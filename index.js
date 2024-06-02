



// var tags=document.getElementsByClassName("nav-link")[0].onClick(Active(this))

// function Active(this){
//     this.classList.add('active-nav-link')

// }

function toggleActive(element) {
    var links = document.querySelectorAll('.nav-link');
    links.forEach(function (link) {
        if (link !== element) {
            link.classList.remove('active-nav-link');
        }
    });
    element.classList.add('active-nav-link');
}





function handleClick(link) {
    console.log("ju8u")
    // Remove 'active' class from all links
    var links = document.querySelectorAll('.nav-link');
    links.forEach(function(link) {
      link.classList.remove('active');
    });

    // Add 'active' class to the clicked link
    link.classList.add('active');
  }

const words = ['Encryption', 'Decryption'];
let index = 0;
const wordElement = document.getElementById('word');

function changeWord() {
    wordElement.textContent = words[index];
    index = (index + 1) % words.length;
}

changeWord(); // Initial word

setInterval(changeWord, 2000); // Change word every 2 seconds




function toggleActive(element) {
   
    element.classList.add('active-nav-link');
}








function toggleEncryptDecrypt() {
    var select = document.getElementById("encrypt-decrypt-select");
    var selectlabel = document.getElementById("label");
    var plaintextInput = document.getElementById("plaintext");
    var keyInput = document.getElementById("key");
    var submitButton = document.getElementById("submit-button");

    if (select.value === "encrypt") {
        plaintextInput.placeholder = "Enter Plaintext to Encrypt";
        keyInput.placeholder = "Enter Key";
        submitButton.innerText = "Encrypt";
        selectlabel.innerText = "Enter Plaintext to Encrypt";
    } else if (select.value === "decrypt") {
        plaintextInput.placeholder = "Enter Ciphertext to Decrypt";
        keyInput.placeholder = "Enter Key";
        submitButton.innerText = "Decrypt";
        selectlabel.innerText = "Enter Ciphertext to Encrypt";
    }
}