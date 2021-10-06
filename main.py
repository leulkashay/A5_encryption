from src.a5_2 import A5_2

if __name__=="__main__":

    key=0xEFCDAB8967452312
    frame_number=0x000134

    

    a5_1=A5_2(key,frame_number)

    (send_key,recive_key)=a5_1.get_key_stream()


    print(send_key)
    print(recive_key)


    print("A5_clock")