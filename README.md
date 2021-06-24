# Formularios con DynamoDB y ses

## para cada nuevo formulario
### template
### app.py

### index 



## desplegado en
https://iydbeoo0t0.execute-api.eu-west-1.amazonaws.com/dev

## para ses

hay que habilitar el envo de corro desde la lambda anacdiendo en el zappa-settings

```json
"extra_permissions": [
      {
        // Attach any extra permissions to this policy.
        "Effect": "Allow",
        "Action": [
          "dynamodb:DescribeStream",
          "dynamodb:GetRecords",
          "dynamodb:GetShardIterator",
          "dynamodb:ListStreams",
          "ses:SendEmail",
          "ses:SendRawEmail"
        ],
        "Resource": "*"
      }
    ],
    "events": [
      {
        "function": "app.send_email_with_attachment",
        "event_source": {
          "arn": "arn:aws:dynamodb:eu-west-1:834787748158:table/clients/stream/2020-12-29T18:02:39.554",
          "enabled": true // Default is false
        }
      }
    ]
  }

```

# casos de fallo

deja de recibir correos he tenido que ir al treigger de dynamo y borrar que habias varios, y volver a activarlo desde la lambda

# como funciona
desde la webapp mete los datos en dynamodb

y con la lambda disparada por dynamodb, envia un correo con los datos 

# para trygger de dynamnoDB
lambda 




# para copiar algunos patrones
https://eu.jotform.com/myforms/?
# FFA_Form
FFA Intake Form, inserts client data into an AWS Dynamodb.  This project uses, HTML5, jQuery, Bootstrap and Flask/Python.



# estructura

