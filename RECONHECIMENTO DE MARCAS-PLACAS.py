import Algorithmia

input = "https://scontent.fsdu6-1.fna.fbcdn.net/v/t1.0-0/p206x206/21151368_837578799757968_8875471011405982811_n.jpg?_nc_cat=110&_nc_eui2=AeHvxxAL60A_2R2P8GSKuXL3nc1Z1e_QyLyNmdnWEjb9EEFGMc5Iu6j21Rwiq8eTniwamm2P4yfFj2h5qTDHkStmpowRVVzbthAn2dcr3rK3uQ&_nc_ht=scontent.fsdu6-1.fna&oh=00a34369951a74ab1db1e10cf746026d&oe=5C72D055"
client = Algorithmia.client('simUZVqt38ilLla2/p89MxMuj9p1')
algo = client.algo('LgoBE/CarMakeandModelRecognition/0.3.15')
print(algo.pipe(input).result)
