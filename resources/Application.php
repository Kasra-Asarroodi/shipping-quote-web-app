

<?php
   require_once "../inc/file_manager.inc.php";
   $animals = get_data('animal.json');
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>"Get started with PETSRUS</title>
    <meta name="Author" content="Kasra Asarroodi, asar0014">
    <meta name="description" content="Happy Paws Animal Shelter Homepage">
    <link rel="stylesheet" href="../style.css">
    <script src="../script.js" defer></script>  
</head>
<body>
  <header>
    <h1>PETSRUS Application</h1>
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
    <h2>Application</h2>
    <p class="subtitle">Start your application process today!</p>
    <div id="error-messages"></div>
    <form method="POST" action="process-application.php" id="application-form">
      <fieldset>
        <legend>Your Details></legend>
        <label for="firstname">First Name:</label>
        <input type="text" id="firstname" name="firstname" required>
        <label for="surname">Surname:</label>
        <input type="text" id="surname" name="surname" required>
        <label for="email">Email:</label>
        <input type="email" placeholder="you@example.com"id="email" name="email" required>
        <label for="phonenumber">Phone Number:</label>
        <input type="tel" id="phonenumber" name="phonenumber" required>
      <fieldset>
        <legend>Select a pet</legend>
        <select id= "pet-id" name= "pet-id">
            <?php foreach ($animals as $animal) { ?>

              <option value="<?= htmlspecialchars($animal['id']) ?>">
                <?= htmlspecialchars ($animal['name']) ?>, 
                <?= htmlspecialchars ($animal['type']) ?>
              </option>
            <?php } ?>
        </select>
      </fieldset>

            
      </fieldset>
      <fieldset>
        <legend> Housing Details</legend>
        <label for="housingtype">Housing Type:</label>
        <select id="housingtype" name="housingtype">
          <option value="house">House</option>
          <option value="apartment">Apartment</option>
          <option value="sharedhouse">Shared House</option>
        </select>
        <p><input type= "radio" id="smYard" name="yardType" value="small">Small Yard</p>
        <p><input type= "radio" id="medYard" name="yardType" value="medium">Medium Yard</p>
        <p><input type= "radio" id="lgYard" name="yardType" value="large">Large Yard</p>
        <label for="PreviousPetExperience">Previous Pet Experience:</label>
        <textarea id="PreviousPetExperience" name="PreviousPetExperience" rows="5" cols="50"></textarea>
      </fieldset>
      <input type="submit" value="Submit Application">
    </form>
   </main>   
  <?php include '../inc/footer.php'; ?>