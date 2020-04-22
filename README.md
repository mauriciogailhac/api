# API

## Running the API

1. Run the following command:

```commandline
docker-compose up -d
```

2. Check if api is running at:

```text
http://127.0.0.1:5000/gloria
```

## Supported Queries and Mutations

### Mutations

1. Add User:

```text
mutation {
        addUser(name:"username str") {
            userId
            name
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
        }
    }
```

3. Remove Contact:

```text
mutation {
        removeContact(contactId:"UUID"){
         ok
         msg
        }
    }
```

4. Remove User:

```text
mutation {
        removeUser(userId:"UUID"){
         ok
         msg
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
            contactId
        }
    }
```

