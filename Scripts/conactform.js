const scriptURL = 'https://script.google.com/macros/s/AKfycbz8xZjZ7R0XbvTySNa92pVIVLQ10F5YiSFs6nwtQJespsPlX-g9jM5T0YKrcPKG7t0j/exec'
const form = document.forms['submit-to-google-sheet']
const msg = document.getElementById("msg")

form.addEventListener('submit', e => {
    e.preventDefault()
    fetch(scriptURL, { method: 'POST', body: new FormData(form)})
    .then(response => {
        msg.innerHTML = "Success" 
        setTimeout(function(){
            msg.innerHTML = ""
    },5000)
    form.reset()
})
    .catch(error => console.error('Error!', error.message))
})