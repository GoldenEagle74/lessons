"""
Повторение - мать учения.
Достаньте имя из словаря
"""
super_dificult_dict = {
    1:{
        "pochti":{
        "Esche chutka":{
            ("Eto","Chto?","kortezh??"):{
                "za chto???":[[1,2,3],["1",2,(13,"oleg")]]
            }
        }
        }
    }
}
while not isinstance(super_dificult_dict, list):
    for k in super_dificult_dict: super_dificult_dict = super_dificult_dict[k]
while not isinstance(super_dificult_dict, str): super_dificult_dict = super_dificult_dict[-1]