
<?php
   require_once "../inc/file_manager.inc.php";
   $animals = get_data('animal.json');
   $apps = get_data ('applications.json');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="../script.js" defer></script>
    <title>"Happy Paws – Admin</title>
    <meta name="Author" content="Kasra Asarroodi, asar0014">
    <meta name="description" content="Happy Paws Animal Shelter Homepage">
    <link rel="stylesheet" href="../style.css">
    
</head>
<div class="login-overlay">
   <div class="login-box">
      <h2> Admin login <h2>
        <label for="email">Email:</label>
        <input type="email" placeholder= "Admin@gmail.com" id="email name="email required>
        <label for="password">Password:</labell>
        <input type="Password" placeholder= "Please enter your password here" id="Password" name="Password" required>
        <button onclick="enterAdmin()">Login</button>
   </div>
</div>

<body>
  <header>
    <h1>PETSRUS ADMIN</h1>
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
  <div id="admin-content" style="display:none;">   
   <main>

    <div id="admin-view">
    <button class="page-select" onclick="showView('animal-view')">View Animals</button>
    <button class="page-select" onclick="showView('app-view')">View Applications</button>
         <div id="animal-view">
           <table>
            <thead>
              <tr>
                <th>Actions</th>
                <th>id</th>
                <th>name</th>
                <th>type</th>
                <th>breed</th>
                <th>status</th>
                <th>image path</th>
              </tr>
            </thead>
           <tbody>

            <?php foreach ($animals as $animal) { ?>

              <tr> 
                   <td> <a class="delete-btn" href="delete-record.php?type=animal&id=<?= urlencode($animal['id']) ?>">Delete</a></td>
                   <td><?= htmlspecialchars($animal['id']) ?></td>
                   <td><?= htmlspecialchars($animal['name']) ?></td>
                   <td><?= htmlspecialchars($animal['type']) ?></td>
                   <td><?= htmlspecialchars($animal['breed']) ?></td>
                   <td><?= htmlspecialchars($animal['status']) ?></td>
                   <td><?= htmlspecialchars($animal['image']) ?></td>
              </tr>
            <?php }?>
           </tbody>
         </table>
       </div>
       <div id="app-view" style="display:none;">
        <table>
           <thead>
             <tr>
               <th>Actions</th>
               <th>ID</th>
               <th>Name</th>
               <th>Email</th>
               <th>Phone</th>
               <th>Date</th>
               <th>Status</th>
             </tr>
           </thead>
           <tbody>

           <?php foreach ($apps as $app) { ?>
              
           
               <?php
               if ($app['status']=='Approved'){
                 $color='green';
                 } else {
                    $color= 'black';
                }

               ?>
  
               <tr> 
                    <td> <a class="delete-btn" href="delete-record.php?type=app&id=<?= urlencode($app['id']) ?>">Delete</a>
                         <a class="approve-btn" href="approve-adoption.php?type=app&app_id=<?= urlencode($app['id']) ?>&pet_id=<?= urlencode($app['pet-id']) ?>">Approve</a>
   
</a>
                    </td>
                    <td><?= htmlspecialchars($app['id']) ?></td>
                    <td><?= htmlspecialchars($app['firstname']) ?></td>
                    <td><?= htmlspecialchars($app['email']) ?></td>
                    <td><?= htmlspecialchars($app['phonenumber']) ?></td>
                    <td><?= htmlspecialchars($app['date']) ?></td>
                    <td style="color: <?= $color ?>;">
                      <?= htmlspecialchars($app['status']?? 'Pending') ?>
                    </td>
               </tr>

             <?php }?>
            </tbody>
          </table>
        </div>
</main>   
</div>  
<?php include '../inc/footer.php'; ?>