import requests

while(True):

    placa = input('Digite a placa do veículo: ')
      
    data = {'placa':placa}
    
    res = requests.get('http://127.0.0.1:9001/veiculos', json=data) 
        
    returned_data = res.json() 
    proprietario = returned_data[0]['proprietario']
    chassi = returned_data[0]['chassi']
    situacao = returned_data[0]['situacao'] 
    #modelo = returned_data['modelo']
    
    print("Informaçoes do veículo - " + "Proprietário: " +proprietario+ " Chassi: "+chassi+" situacao: "+situacao)
    #print(returned_data[0])