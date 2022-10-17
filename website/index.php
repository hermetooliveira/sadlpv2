<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SADLPV - Trabalho de Conclusão de Curso</title>
</head>
<body>
    <?php
        $result = file_get_contents("http://node-container:9001/veiculos");
        $veiculos = json_decode($result)
    ?>
    <table>
        <thead>
            <tr>
                <th>Proprietário</th>
                <th>Placa</th>
                <th>Chassi</th>
                <th>situação</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach($veiculos as $veiculo): ?>
                <tr>
                    <td><?php echo $veiculo->proprietario; ?></td>
                    <td><?php echo $veiculo->placa; ?></td>
                    <td><?php echo $veiculo->chassi; ?></td>
                    <td><?php echo $veiculo->situacao; ?></td>                    
                </tr>
            <?php endforeach?>    
        </tbody>
    </table>
</body>
</html>