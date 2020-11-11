<?php
try {
    (new PharData('out.tar.gz'))->decompress();
    (new PharData('out.tar')->extractTo('.', null, true);
    echo 'Done';
} catch (Exception $e) {
    echo 'Error' . print_r($e);
}
?>