<?php
   require_once "../inc/file_manager.inc.php";


 if (isset($_GET['app_id']) && isset($_GET['pet_id'])) {
    $pet_id=$_GET['pet_id'];
    $app_id=$_GET['app_id'];

    $apps=get_data('applications.json');
    $animals=get_data('animal.json');

    foreach ($animals as &$animal) {
          if ($animal['id']== $pet_id) {
            $animal['status'] = 'Adopted';
            break;
          }

    }

    save_data('animal.json', $animals);
 


    foreach ($apps as &$app) {
          if ($app['id']==$app_id) {
              $app['status'] = 'Approved';
              break;
          }
    }

    save_data('applications.json', $apps);

    $log=get_data('adoptions-log.json');
    $log[] = [
    "date" => date("Y-m-d H:i:s"),
    "app_id" => $app_id,
    "pet_id" => $pet_id
];

    save_data('adoptions-log.json', $log);
    header("Location: admin.php");
    exit();
}
?>

