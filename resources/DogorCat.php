<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>"Choose your pet!</title>
    <meta name="Author" content="Kasra Asarroodi, asar0014">
    <meta name="description" content="Happy Paws Animal Shelter Homepage">
    <link rel="stylesheet" href="../style.css">
    <script src="../script.js" defer></script>
</head>
<body>
  <header>
    <h1>Select your desired animal you would wish to look into more</h1>
       <img src="../imgs/HEADING-ELEMENT.png" alt="PETSRUS Logo"><br>  
  </header> 
    <nav>
        <ul>
            <li><a href="../Index.php">Home</a></li>
            <li><a href="Application.php">Application</a></li>
            <li><a href="Aboutus.php">About Us</a></li>
            <li><a href="contactus.php">Contact Us</a></li>
            <li><a href="admin.php">Admin</a></li>
        </ul> 
      </nav>
   <main>
    <h2>What type of pet are you looking for?</h2>
    <p class="subtitle">Click on the image to see the available pets of that type!</p>
    <div class="dogorcat-image">
            <div class="Cat-Dog-image">
              <a href="PetlistDog.php"><img src="../imgs/DogorCat-Dog.png" alt="DOG Image"></a>
            </div>
            <h3>Our Pets are waiting for you!</h3>
            <div class="Cat-Dog-image">
              <a href="PetlistCat.php"><img src="../imgs/DogorCat-Cat.png" alt="CAT Image"></a>
            </div>
    </div>
  </main>
  <?php include '../inc/footer.php'; ?>