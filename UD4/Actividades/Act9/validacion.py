import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "Asignaturas": {
            "type": "object",
            "properties": {
                "Asignatura": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "nombre_asignatura": {
                                "type": "string"
                            },
                            "temas": {
                                "type": "object",
                                "properties": {
                                    "tema": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "numero_tema": {
                                                    "type": "string"
                                                },
                                                "titulo_tema": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": ["numero_tema", "titulo_tema"]
                                        }
                                    }
                                },
                                "required": ["tema"]
                            }
                        },
                        "required": ["nombre_asignatura", "temas"]
                    }
                }
            },
            "required": ["Asignatura"]
        }
    },
    "required": ["Asignaturas"]
}

# Archivo JSON a validar
archivo_json = '''
{
  "Asignaturas": {
      "Asignatura": [
        {
          "nombre_asignatura": "Lengua",
          "temas": {
            "tema": [
              {
                "numero_tema": "tema1",
                "titulo_tema": "Los niveles de la lengua"
              },
              {
                "numero_tema": "tema2",
                "titulo_tema": "Origen y desarrollo de la Lengua Española"
              },
              {
                "numero_tema": "tema3",
                "titulo_tema": "Situación lingüística de España. Lenguas y dialectos"
              },
              {
                "numero_tema": "tema4",
                "titulo_tema": "Variedad dialectal extremeña"
              },
              {
                "numero_tema": "tema5",
                "titulo_tema": "Características del español de América"
              },
              {
                "numero_tema": "tema6",
                "titulo_tema": "Procedimientos de creación de palabras"
              }
            ]
          }
        },
        {
          "nombre_asignatura": "Matemáticas",
          "temas": {
            "tema": [
              {
                "numero_tema": "tema1",
                "titulo_tema": "Matrices"
              },
              {
                "numero_tema": "tema2",
                "titulo_tema": "Inecuaciones y sistemas"
              },
              {
                "numero_tema": "tema3",
                "titulo_tema": "Determinantes"
              },
              {
                "numero_tema": "tema4",
                "titulo_tema": "Programación lineal"
              }
            ]
          }
        },
        {
            "nombre_asignatura": "Matemáticas",
            "temas": {
              "tema": [
                {
                  "numero_tema": "tema1",
                  "titulo_tema": "Matrices"
                },
                {
                  "numero_tema": "tema2",
                  "titulo_tema": "Inecuaciones y sistemas"
                },
                {
                  "numero_tema": "tema3",
                  "titulo_tema": "Determinantes"
                },
                {
                  "numero_tema": "tema4",
                  "titulo_tema": "Programación lineal"
                }
              ]
            }
          },
          {
            "nombre_asignatura": "Matemáticas",
            "temas": {
              "tema": [
                {
                  "numero_tema": "tema1",
                  "titulo_tema": "Matrices"
                },
                {
                  "numero_tema": "tema2",
                  "titulo_tema": "Inecuaciones y sistemas"
                },
                {
                  "numero_tema": "tema3",
                  "titulo_tema": "Determinantes"
                },
                {
                  "numero_tema": "tema4",
                  "titulo_tema": "Programación lineal"
                }
              ]
            }
          },
          {
            "nombre_asignatura": "Dibujo_Tecnico",
            "temas": {
              "tema": [
                {
                  "numero_tema": "tema1",
                  "titulo_tema": "Trazados fundamentales en el plano"
                },
                {
                  "numero_tema": "tema2",
                  "titulo_tema": "Potencia, eje radical"
                },
                {
                  "numero_tema": "tema3",
                  "titulo_tema": "Polígonos. Triángulos"
                },
                {
                  "numero_tema": "tema4",
                  "titulo_tema": "Equivalencias."
                },
                {
                  "numero_tema": "tema5",
                  "titulo_tema": "Homología y afinidad"
                },
                {
                  "numero_tema": "tema6",
                  "titulo_tema": "Inversión"
                }
              ]
            }
          },
          {
            "nombre_asignatura": "TIC",
            "temas": {
              "tema": [
                {
                  "numero_tema": "tema1",
                  "titulo_tema": "Definición y tipos de estructuras de almacenamiento"
                },
                {
                  "numero_tema": "tema2",
                  "titulo_tema": "Características de las principales estructuras de almacenamiento"
                },
                {
                  "numero_tema": "tema3",
                  "titulo_tema": "Aplicaciones de las estructuras de almacenamiento"
                },
                {
                  "numero_tema": "tema4",
                  "titulo_tema": "Introducción a los lenguajes de programación"
                },
                {
                  "numero_tema": "tema5",
                  "titulo_tema": "Sintaxis y semántica"
                },
                {
                  "numero_tema": "tema6",
                  "titulo_tema": "Programación estructurada general"
                }
              ]
            }
          },
          {
            "nombre_asignatura": "Historia de España",
            "temas": {
              "tema": [
                {
                  "numero_tema": "tema1",
                  "titulo_tema": "Prehistoria en la Península Ibérica"
                },
                {
                  "numero_tema": "tema2",
                  "titulo_tema": "Imperio romano en la Península Ibérica"
                },
                {
                  "numero_tema": "tema3",
                  "titulo_tema": "Monarquía visigoda"
                },
                {
                  "numero_tema": "tema4",
                  "titulo_tema": "Edad Media en España"
                }
              ]
            }
          },
          {
            "nombre_asignatura": "Religion",
            "temas": {
              "tema": [
                {
                  "numero_tema": "tema1",
                  "titulo_tema": "Antropología cristiana"
                },
                {
                  "numero_tema": "tema2",
                  "titulo_tema": "Doctrina social de la Iglesia"
                },
                {
                  "numero_tema": "tema3",
                  "titulo_tema": "Relación entre la razón, la ciencia y la fe"
                },
                {
                  "numero_tema": "tema4",
                  "titulo_tema": "La Iglesia generadora de cultura a lo largo de la historia"
                },
                {
                  "numero_tema": "tema5",
                  "titulo_tema": "La Biblia, la escritura sagrada"
                }
              ]
            }
          },
          {
            "nombre_asignatura": "Fisica",
            "temas": {
              "tema": [
                {
                  "numero_tema": "tema1",
                  "titulo_tema": "Gravitación universal"
                },
                {
                  "numero_tema": "tema2",
                  "titulo_tema": "Movimiento armónico simple"
                },
                {
                  "numero_tema": "tema3",
                  "titulo_tema": "Movimiento ondulatorio"
                }
              ]
            }
          }
    
      ]
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
