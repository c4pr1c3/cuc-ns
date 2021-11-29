<?php

$logger = "/tmp/logger.txt";

if (array_key_exists("input", $_REQUEST)) {
        file_put_contents($logger, 'IP: ' . $_SERVER['REMOTE_ADDR'] . 'Date: ' . date('Y-m-d H:i:s', time()) . ", Text: " . $_REQUEST['input']. "\n", FILE_APPEND);
        var_dump($_REQUEST['input']);
}
?><html>
<head>
    <meta http-equiv="refresh" content="5"/>
</head>
<body>
    <?= nl2br(@file_get_contents($logger)); ?>
</body>
</html>