# Dashain Greetings 
Dashain Greetings Api provides list of greetings for *Dashain Festival*

# Endpoints:

## All greetings
[https://dashain.herokuapp.com/api/greetings/](https://dashain.herokuapp.com/api/greetings/)

## Greetings by id (int:id)
[https://dashain.herokuapp.com/api/greetings/1](https://dashain.herokuapp.com/api/greetings/1)


## Greetings by language
1. Nepali:
    [https://dashain.herokuapp.com/api/greetings/lang/nepali](https://dashain.herokuapp.com/api/greetings/lang/nepali)
2. English:
    [https://dashain.herokuapp.com/api/greetings/lang/nepali](https://dashain.herokuapp.com/api/greetings/lang/nepali)

## Random greetings
[https://dashain.herokuapp.com/api/greetings/random](https://dashain.herokuapp.com/api/greetings/random)

## Language specific random greetings
1. [https://dashain.herokuapp.com/api/greetings/lang/nepali/random](https://dashain.herokuapp.com/api/greetings/lang/nepali/random)
2. [https://dashain.herokuapp.com/api/greetings/lang/english](https://dashain.herokuapp.com/api/greetings/lang/english)

## How these greetings were collected
The majority of greetings were contributed!

## Make a contribution!
Submit a Pull Request, with your greeting added to the greetings/index.json file. Make sure the greeting is in this format:
```
{
    "id": last greeting id + 1,
    "language": "nepali",
    "greeting": "Greeting here...."
}
```

## Inspired from
This API was inspired from [15Dkatz/official_joke_api](https://github.com/15Dkatz/official_joke_api)