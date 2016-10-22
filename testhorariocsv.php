<?php
$today = new DateTime();

$nl = "\n";

$csv = fopen('horarios.csv','w+');
for($i=0 ; $i < 100 ; $i++){
	$endDay = $today->add(new DateInterval('PT2H'));
	fwrite($csv, '"",'.'"'.$today->format('Y-m-d H:i:s').'","'.$endDay->format('Y-m-d H:i:s').'",1'.$nl);
	$i++;
	$today = $today->add(new DateInterval('P'.$i.'D'));
}
fclose($csv);
?>
