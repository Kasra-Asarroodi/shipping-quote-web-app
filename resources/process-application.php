<?php

require_once "../inc/file_manager.inc.php";


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $apps = get_data('applications.json');
  
  
  $new_app = [
    'id' => uniqid('APP-'),
    'firstname' => htmlspecialchars($_POST['firstname']),
    'surname' => htmlspecialchars($_POST['surname']),
    'email' => htmlspecialchars($_POST['email']),
    'phonenumber' => htmlspecialchars($_POST['phonenumber']),
    'pet-id' => htmlspecialchars($_POST['pet-id']),
    'housingtype' => htmlspecialchars($_POST['housingtype']),
    'yardType' => htmlspecialchars($_POST['yardType']),
    'status'=> 'Pending',
    'PreviousPetExperience'=> htmlspecialchars ($_POST['PreviousPetExperience']),
    'date' => date('Y-m-d H:i:s')
];



  $apps[] = $new_app;


  save_data('applications.json', $apps);
  header("Location: ../Index.php");
  exit();

}
?>