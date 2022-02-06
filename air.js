const credentials = {
    apiKey: '32274c0a9472cd5d07a9d60f9454d7e4b3bd4d5e448c4d7d08459211e9aab89f',
    username: 'sandbox'
}

const AfricasTalking = require('africastalking')(credentials)

const airtime = AfricasTalking.AIRTIME

const options = {
    recipients: [{
        phoneNumber: "0795388701",
        currencyCode: "KES",
        amount: "100"
    }]
};

airtime.send(options)
    .then( response => {
        console.log(response);
    })
    .catch( error => {
        console.log(error);
    });