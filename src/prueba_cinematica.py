from cinematica.kine import Kine 

if __name__ == "__main__":
    kn = Kine()
    #directa
    kn.apply_f_kinematics()
    #inversa
    kn.apply_inv_kinematics(0.066,-0.400,0.421)

    pos_start =[0.0,0.0,0.0,0.0,0.0]
    pos_desired =[45.0,45.0,45.0,45.0,45.0]
    steps = 5

    result = kn.path_plannig(pos_start,pos_desired,steps)
    for array in result:
        print(array)