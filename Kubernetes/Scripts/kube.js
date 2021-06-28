function clear_in() {
    document.getElementById('in').value = "";
}

// Loader method
window.addEventListener("keyup", function (event) {
    if (event.key == 'Enter') {
        const loader = document.getElementById("loader");
        resource(event);
    }
})



function displayloader() {
    loader.classList.add("display");
    // setTimeout(() => {
    //     loader.classList.remove("display");
    // }, 10000);
}

function hideloader() {
    loader.classList.remove("display")
}
// loader ends

function resource(event) {

    value = document.getElementById("in").value;
    xhr = new XMLHttpRequest();
    xhr.open("GET", "192.168.99.111/../../cgi-bin/kube.py?value=" + value, true);
    xhr.send();
    displayloader()
    xhr.onload = function () {
        var output = xhr.responseText;
        hideloader()
        document.getElementById("resource").innerHTML = output;
    }
}
