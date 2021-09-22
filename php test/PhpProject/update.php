<?php
	$servername = "localhost";//  設定要連的伺服器位置
	$username = "root";//  登錄使用的使用者姓名
	$password = "1234";//  設定登錄的使用者密碼
	$dbname = "myDB";//設定要抓取的資料庫
	
	$Id =$_REQUEST['Id'];//設定預設id
	$Name = $_REQUEST['Name'];//設定預設name
	$Count = $_REQUEST['Count'];
	$Age = $_REQUEST['Age'];
	$Email = $_REQUEST['Email'];//設定預設email
	
	$conn = mysql_connect($servername, $username, $password) or die('Error with MySQL connection');//如果沒偵測到servername,username,password，則跳出Error with MySQL connection的錯誤
	mysql_query("SET NAMES 'utf8'");//設定 utf8的編碼
	mysql_select_db($dbname);// 選擇 剛設定的$dbname 裡的myDB資料庫
	$sql_update = "Update worktable Set  Name = '$Name', Count = '$Count', Age = '$Age', Email = '$Email' WHERE Id = '$Id'"; //設定SQL指令
	$result = mysql_query($sql_update) or die('MySQL update error'); // 如果沒設定成功的SQL指令則跳出MySQL update error的錯誤
	
	$sql_query = "select * from worktable";//設定抓取的資料表
	$result = mysql_query($sql_query) or die('MySQL worktable error');// 如果設定的資料表沒抓取到則跳出 MySQL mysecond error的錯誤
	
	echo "<table border='1'>
	<tr>
	<th>Id</th>
	<th>Name</th>
	<th>Count</th>
	<th>Age</th>
	<th>Email</th>
	</tr>";
	
		while($row = mysql_fetch_array($result)){//函數將 結果行mysql_fetch_array 作為關聯
			echo "<tr>";// 將內容隔開
			echo "<td>" . $row['Id'] . "</td>";//將內容插入這一行
			echo "<td>" . $row['Name'] . "</td>";//將內容插入這一行
			echo "<td>" . $row['Count'] . "</td>";
			echo "<td>" . $row['Age'] . "</td>";
			echo "<td>" . $row['Email'] . "</td>";//將內容插入這一行
			echo "</tr>";  // 將內容隔開
		}
		echo "</table>";
		mysql_close($conn);//所設定的內容最後關閉，如果設定錯誤則Error with MySQL connection的錯誤
?>



