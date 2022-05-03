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
        client.subscribe(TOPIC)

    else:
        print("[{}]Error al conectarse al servidor".format(_API_NAME_))



def on_disconnected(client,userdata,rc):

    if rc !=0:

        print("[{}] desconectado del servidor".format(_API_NAME_))


def on_message(client, userdata, msg):
    print("mensaje recibido:")
    buffer = str(msg.payload.decode("utf-8"))
    print("mensaje recibido {}".format(buffer))





def Main():
    print(_API_NAME_)
    client = mqtt.Client(client_id = "simo-test", clean_session= False)
    print("conectado con {} mediante puerto {}".format(URL,PORT))
    client.on_connect = on_connect
    client.on_disconnected = on_disconnected
    client.on_message = on_message

    client.username_pw_set(ID,PASS)
    client.connect(host = URL,port = PORT, keepalive = 60)
    client.loop_forever()






if __name__ == "__main__":
    Main()

    