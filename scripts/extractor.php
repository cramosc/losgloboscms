<?php
try {
    $phar = new PharData('out.tar.gz');
    $phar->decompress();
    
    $phar = new PharData('out.tar');
    $phar->extractTo('.', null, true);

    echo 'Done';
} catch (Exception $e) {
    echo 'Error' . print_r($e);
}
?>