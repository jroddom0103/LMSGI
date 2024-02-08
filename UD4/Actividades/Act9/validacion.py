import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "nombre": {
      "type": "string",
      "minLength":  0
    },
    "edad": {
      "type": "integer",
      "minimum":  0
    },
    "hobbies": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "correo": {
      "type": "string",
      "format": "email"
    },
    "sexo": {
      "type": "string",
      "enum": ["H", "M"]
    }
  },
  "required": ["nombre", "edad", "hobbies", "correo", "sexo"]
}

# Archivo JSON a validar
archivo_json = '''
{
  "nombre": "Juan",
  "edad":  25,
  "hobbies": ["lectura", "ciclismo"],
  "correo": "jroddom0103@g.educaand.es",
  "sexo": "H"
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.
