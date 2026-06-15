<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>"PETSRUS-About Us</title>
    <meta name="Author" content="Kasra Asarroodi, asar0014">
    <meta name="description" content="Happy Paws Animal Shelter Homepage">
    <link rel="stylesheet" href="../style.css">
    <script>const defaultType = "Cat";</script>
    <script src="../script.js" defer></script>
    
</head>
<body>
  <header>
    <h1>About Us</h1>
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
    <h2>Our Cats waiting are looking for a home!</h2>
     <p class="list subtitle">Click on the Cat you are interested in</p>
     <div>
      <div class="Filter-box">
      <input type=" "text placeholder="Search by name" id="search-name">

      <label for="Filter by type">Filter by type</label>

      <select id="filter-type">
        <option value="All">All Types</option>
        <option value="Dog">Dogs</option>
        <option value="Cat">Cats</option>
      </select>
     </div>
     <div id="animal-container"></div>
    </div>
  </main>
  <?php include '../inc/footer.php'; ?>