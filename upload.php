if ($_FILES['file']['error'] === UPLOAD_ERR_OK) {
  $tmp_name = $_FILES['file']['tmp_name'];
  $name = basename($_FILES['file']['name']);
  move_uploaded_file($tmp_name, "uploads/$name");
  echo "File uploaded successfully.";
} else {
  echo "Error uploading file.";
}
?>