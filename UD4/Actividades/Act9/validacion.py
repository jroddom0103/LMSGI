import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "root": {
            "type": "object",
            "properties": {
                "@xmlns:ap1": {
                    "const": "PrimerApellido"
                },
                "@xmlns:ap2": {
                    "const": "SegundoApellido"
                },
                "películas": {
                    "type": "object",
                    "properties": {
                        "película": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "@id": {
                                        "type": "string"
                                    },
                                    "nombre": {
                                        "type": "string"
                                    },
                                    "director": {
                                        "type": "string"
                                    },
                                    "tema": {
                                        "type": "string"
                                    },
                                    "fechaEstreno": {
                                        "type": "string",
                                        "pattern": "^\\d{1,2}/\\d{1,2}/\\d{4}$"
                                    },
                                    "actores": {
                                        "type": "object",
                                        "properties": {
                                            "actor": {
                                                "type": "array",
                                                "items": {
                                                    "type": "object",
                                                    "properties": {
                                                        "ap1:apellido": {
                                                            "type": "string"
                                                        },
                                                        "ap2:apellido": {
                                                            "type": "string"
                                                        },
                                                        "nombre": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": ["ap1:apellido", "ap2:apellido", "nombre"]
                                                }
                                            }
                                        },
                                        "required": ["actor"]
                                    },
                                    "productora": {
                                        "type": "string"
                                    }
                                },
                                "required": ["@id", "nombre", "director", "tema", "fechaEstreno", "actores", "productora"]
                            }
                        }
                    },
                    "required": ["película"]
                }
            },
            "required": ["@xmlns:ap1", "@xmlns:ap2", "películas"]
        }
    },
    "required": ["root"]
}

# Archivo JSON a validar
archivo_json = '''
{
  "root": {
        "@xmlns:ap1": "PrimerApellido",
        "@xmlns:ap2": "SegundoApellido",
        "películas": {
            "película": [
                {
                    "@id": "1",
                    "nombre": "El Padrino",
                    "director": "Francis Ford Coppola",
                    "tema": "Mafia",
                    "fechaEstreno": "20/10/1972",
                    "actores": {
                        "actor": [
                            {
                                "ap1:apellido": "James",
                                "ap2:apellido": "Pacino",
                                "nombre": "Alfredo"
                            },
                            {
                                "ap1:apellido": "Brando",
                                "ap2:apellido": "Jr.",
                                "nombre": "Marlon"
                            }
                        ]
                    },
                    "productora": "Paramount Pictures"
                },
                {
                    "@id": "10",
                    "nombre": "El Señor de los Anillos: la Comunidad del Anillo",
                    "director": "Peter Jackson",
                    "tema": "Fantasía",
                    "fechaEstreno": "19/12/2001",
                    "actores": {
                        "actor": [
                            {
                                "ap1:apellido": "Jordan",
                                "ap2:apellido": "Wood",
                                "nombre": "Elijah"
                            },
                            {
                                "ap1:apellido": "Mortensen",
                                "ap2:apellido": "Jr.",
                                "nombre": "Viggo Peter"
                            }
                        ]
                    },
                    "productora": "New Line Cinema"
                }
            ]
        }
    }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
