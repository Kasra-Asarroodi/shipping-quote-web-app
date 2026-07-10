
console.log ("kasra");
const animalContainer = document.getElementById("quoteinfo");

function renderAnimals(quoteInfo){
    if (!quoteInfo)return;
   
   
    quoteinformation.innerHTML= '';
     
    animalList.forEach (quote => {  
       const quotehtmll= `
       <a href= "${quote.price}" class="animal-card-link">
        <div class="quote-card">
          <p><strong>Name:</strong>${quote.sendername}</p>
          <p><strong>Status:</strong>${quote.price}</p>
          <p><strong>Breed:</strong>${quote.senderPHONE}</p>
        </div>
      `;
       animalContainer.innerHTML += cardHTML;
     }); 
}



if (animalContainer && typeof defaultType !== "undefined") {
  const initialAnimals = animals.filter(animal => animal.Type === defaultType);
  renderAnimals(initialAnimals);
}

const searchInput = document.getElementById ('search-name');
const typeDropdown = document.getElementById ('filter-type');

function handleFilter () {

  const searchTerm = searchInput.value.toLowerCase();
  const selectedType = typeDropdown.value;

  const filtered = animals.filter (animal => {
    const matchesName = animal.Name.toLowerCase().includes(searchTerm);

    const matchesType= selectedType === 'All' || animal.Type === selectedType;

   return matchesName && matchesType
  


  });

renderAnimals(filtered);

}


 if (searchInput && typeDropdown){
    searchInput.addEventListener('input', handleFilter);
    typeDropdown.addEventListener('change', handleFilter);
 }


const errorPromo = document.getElementById ("error-promo");
const promoForm = document.getElementById ("promorate");
const promoRate = document.getElementById("promo-rate");

if (promoRate && promoForm) {
  promoForm.addEventListener('submit', (e) => {
    let errors = [];
    const promoValue = Number(promoRate.value);
    if (promoValue > 100 || promoValue < 0 || Number.isNaN(promoValue)) {
        errors.push("Promotion discount must be between 0 to 100%");
    }
  
    if (errors.length > 0) {
          e.preventDefault();
          errorPromo.style.display = "block";
  
    }
  });
}








const quoteInfo = document.getElementById ("quote-info");
const errorMsgs = document.getElementById ("error-messages");

if (quoteInfo) {
  quoteInfo.addEventListener('submit', (e) => {
    let errors= [];
  
  
    const weight = document.getElementById("weight").value;
    const makeups = document.getElementById("makeups").value;
    const electronics = document.getElementById("electronics").value;
    const value = document.getElementById("value").value;
    const medications = document.getElementById("medications").value;

    const senderNAME = document.getElementById("sendername").value;
    const senderPHONE = document.getElementById("senderphone").value;
    const senderEMAIL = document.getElementById("senderemail").value;

    const receiverNAME = document.getElementById("receivername").value;
    const receiverPHONE = document.getElementById("receiverphone").value;
    const receiverEMAIL = document.getElementById("receiveremail").value;
    const receiverADDRESS = document.getElementById("receiveraddress").value;


    if (weight === "" || weight > 25) {
        errors.push("Weight must be greater than 0 and less than 25kg");
    }

    if (value === "" || value <= 0) {
        errors.push("Total value must be greater than 0.");
    }

    if (medications < 0) {
        errors.push("Number of medications cannot be negative.");
    }

    if ( makeups < 0) {
        errors.push("Number of makeup products cannot be negative.");
    }

    if ( electronics < 0) {
        errors.push("Number of laptops or cellular devices cannot be negative.");
    }


    if (senderNAME === "") {
      errors.push ("Please ensure to enter your name and last name!");
    }

    if (senderPHONE === "") {
      errors.push ("Please ensure to enter your phone number!");
    }

    if (senderEMAIL === "") {
      errors.push ("Please ensure to enter your email!");
    }


    if (receiverPHONE !== "") {
         if (isNAN(receiverPHONE)){
            errors.push ("Please ensure to enter a valid phone number!");
         }
    }

    if (receiverNAME !== "") {

        if (
           receiverNAME.includes("0") ||
           receiverNAME.includes("1") ||
           receiverNAME.includes("2") ||
           receiverNAME.includes("3") ||
           receiverNAME.includes("4") ||
           receiverNAME.includes("5") ||
           receiverNAME.includes("6") ||
           receiverNAME.includes("7") ||
           receiverNAME.includes("8") ||
           receiverNAME.includes("9")
        ) {
           errors.push("Receiver name cannot contain numbers");
        }
}
     

  



    if (errors.length > 0) {
        e.preventDefault();
        errorMsgs.style.display = "block";
        errorMsgs.innerHTML = errors.join("<br>");
    }
  });
}









function openSenderPopup() {
    document.getElementById("senderPopup").style.display = "block";
}

function closeSenderPopup() {
    document.getElementById("senderPopup").style.display = "none";
}

function openReceiverPopup() {
    document.getElementById("receiverPopup").style.display = "block";
}

function closeReceiverPopup() {
    document.getElementById("receiverPopup").style.display = "none";
}





function openPopup() {
    document.getElementById("loginOverlay").style.display = "flex";
}

function closePopup() {
    document.getElementById("loginOverlay").style.display = "none";
}






setTimeout(function () {
  const popup = document.getElementById("popupMessage");

  if (popup) {
    popup.style.display = "none";
  }
}, 3000);