# API

## Running the API

### Docker

1. Run the following command:

```commandline
docker-compose up -d
```

2. Check if api is running at:

```text
http://127.0.0.1:5000/gloria
```

### Virtualenv

1. Install virtualenv in your system.

2. Install postgresql in your system.

3. Create user "admin", password "admin" and db "gloria" on postgresql.

4. Make sure that postgresql is running on port 5432.

5. Create a virtualenv inside the project directory using the following command:

```commandline
virtualenv . -p path/to/python3/interpreter
```

6. Activate the virtualenv:

```commandline
source bin/activate
```

7. Install python packages:

```commandline
pip install -r src/requirements.txt
```

8. Run the api:

```commandline
python src/gloria.py
```

## Supported Queries and Mutations

### Mutations

1. Add User:

```text
mutation {
        addUser(name:"username str") {
            userId
            name
            error
        }
}

```

2. Add Contact:

```text
mutation {
        addContacts(
            input: [
                {
                   userId:"UUID"
                   name: "Str"
                   contactData:[
                        {
                            type:"phone",
                            value:"123"
                        },
                        {
                            type:"email",
                            value:"test@test.com"
                        }
                    ]
                }
            ]
        ) {
            contacts {
                contact {
                    contactId
                    userId
                    name
                    contactData {
                        type
                        value
                    }
                }

            }
            error
        }
    }
```

3. Remove Contact:

```text
mutation {
        removeContact(contactId:"UUID"){
         ok
         error
        }
    }
```

4. Remove User:

```text
mutation {
        removeUser(userId:"UUID"){
         ok
         error
        }
    }
```

### Queries

1. Get User:

```text
query {
        getUser(name:"str") {
            userId
            name
            contacts{
              contactId
              name
              contactData{
            	  type
                  value
              }

            }

        }
    }
```

2. Get Contact:

```text
query {
        getContact(contactId:"UUID") {
            contactId
            name
            userId
            contactData {
                type
                value
            }
        }
    }
```

3. Match Contacts:

```text
query {
        matchContact(
            input:{
                contactData:[
                    {
                        type:"phone",
                        value:"123"
                    },
                    {
                        type:"email",
                        value:"test@test.com"
                    }
                ]
            }
        ) {
            contactId
            userId
            name
            contactData {
                type
                value
            }
        }
    }
```

4. Get all users:

```text
query {
        allUsers {
            userId
            name
        }
    }
```

5. Get all Contacts:

```text
query {
        allContacts {
            contactId
            userId
            name
            contactData{
              type
              value
            }
        }
    }

```

6. Get all ContactData:

```text
query {
        allContactData {
            type
            value
            contactid
        }
    }
```

