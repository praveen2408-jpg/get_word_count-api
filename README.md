# get_word_count-api
get_word_count api


Create a Flask POST API function which will return word count of each word in the text passed to it.

Sample:

HTTP: POST 

Following needs to be passed to the API

POST http://localhost:8000/get_word_count

Sample
Case #1:
Body of POST Request:
{
     'text' : 'This is a good day. I need to have more good days like this.'
}

Response:
{

'text': {
    'This' : 1,
    'is' : 1,
    'good' : 2,
    .
    . }
}

Case #2:
If Body of POST request is empty, Response:
{
'No text received'
}

Case#3:
Body of POST Request:
{
     'text1' : 'This is a good day. I need to have more good days like this.',
     'text2' : 'Some new line',
    'text3' : 'Some other line'
}

Response:
{

'text1': {
    'This' : 1,
    'is' : 1,
    'good' : 2,
    .
    . } ,
'text2': {
    'This' : 1,
    'is' : 1,
    'good' : 2,
    .
    . },
'text3': {
    'This' : 1,
    'is' : 1,
    'good' : 2,
    .
    . }
}

