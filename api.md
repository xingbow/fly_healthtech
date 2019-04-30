# _API reference_

update your api reference here

---
## Some examples

## POST _/api/auth/register_ 

post body
``` json
{
    "userName": "test",
    "password": "test",
    "kindergarten": "test_kindergarten"
}
```

return body
``` json
{
    "success": true,
    "userId": "test"
}
```
``` json
{
    "success": false,
    "message": "This username has been existed."
}
```


## POST _/api/info/user/\<userId>/profile_?token=
update password or kindergarten

``` json
{
    "userName": "test",
    "password": "test",
    "kindergarten": "test_kindergarten"
}
```

return body
``` json
{
    "success": true,
    "userId": "test"
}
```
``` json
{
    "success": false,
}
```