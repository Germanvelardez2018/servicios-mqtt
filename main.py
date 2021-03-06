# Servicios MQTT

import paho.mqtt.client as mqtt
import time



# Credenciales
TOPIC = "SIMO_CONFIG"
URL = "simointi.cloud.shiftr.io"
PASS = "fdZY5b69OhOVsAns"
ID = "simointi"
PORT = 1883
_API_NAME_ = "servicios mqtt"





#------------------------ Callback functions


def on_connect(client,userdata,flags,rc):
    if rc==0:

        print("[{}] conectado con el servidor".format(_API_NAME_))
        print("[{}] Publicando mensajes en el topic {}".format(_API_NAME_,TOPIC))
    else:
        print("[{}]Error al conectarse al servidor".format(_API_NAME_))



def on_disconnected(client,userdata,rc):

    if rc !=0:

        print("[{}] desconectado del servidor".format(_API_NAME_))





def Main():
    print(_API_NAME_)
    client = mqtt.Client(client_id = "simo-config", clean_session= False)
    print("conectado con {} mediante puerto {}".format(URL,PORT))
    client.on_connect = on_connect
    client.on_disconnected = on_disconnected
    client.username_pw_set(ID,PASS)
    client.connect(host = URL,port = PORT, keepalive = 60)



    counter = 0 

    while True:
        print("Envio {} al topico {}".format(counter,TOPIC))
        client.publish(TOPIC,"contador: {}".format(counter))
        counter += 1
        time.sleep(10)




if __name__ == "__main__":
    Main()

    