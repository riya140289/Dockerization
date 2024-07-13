

function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        
        if(response.status == 200){
            window.location.href = '/'
        }
        else{
            alert(response.message)
        }

    })

}


function register(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value
    var firstname = document.getElementById('FirstName').value
    var lastname = document.getElementById('LastName').value
    if(username == '' && password == '' && firstname == '' && lastname ==''){
        alert('You must enter all data')
    }

    var data = {
        'username' : username,
        'password' : password,
        'firstname' : firstname,
        'lastname'  : lastname
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
          alert(response.message)
        }
        else{
            alert(response.message)
        }

    })

}