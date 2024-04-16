function lockUi(){
    authbox = document.createElement('div')
    passwd = document.createElement('input')
    submbtn = document.createElement('input')
    
    passwd.type = 'password'
    passwd.name = 'passwd'

    submbtn.type = 'submit'
    submbtn.type = 'Login'
    
    authbox.appendChild(submbtn)
    authbox.appendChild(passwd)
    
    return authbox
}