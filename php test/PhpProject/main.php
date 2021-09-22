<!DOCTYPE HTML>   
<html>            
<head>            
<title>資料庫管理</title>  
</head>            
<body>             
<?php               
  echo '請輸入資料'."<p>";      
 ?>                 
	<form action="" name="form1" method="Post">            
	Id：<Input Type="text" Name="Id"> <p>        
	Name：<Input Type="text" Name="Name"> <p>
	Count：<Input Type="text" Name="Count"> <p>
	Age：<Input Type="text" Name="Age"><p>
	Email：<Input Type="text" Name="Email"><p>  
	<input type="button" value="新增" type="submit" onclick="form1.action='insert1.php';form1.submit();"/>
	<br><br> 
	<input type="button" value="查詢項目" type="submit" onclick="form1.action='select.php';form1.submit();"/>   
	</form>
</body>
</html>


