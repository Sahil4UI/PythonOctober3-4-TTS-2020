data=[
        {"id":101,"Name":"Navya","Marks":[90,80,70]},
        {"id":102,"Name":"Sahil","Marks":[95,89,78]},
        {"id":103,"Name":"Vishal","Marks":[10,19,0]},
        {"id":104,"Name":"Navya","Marks":[70,60,50]},
        {"id":105,"Name":"Navya","Marks":[80,50,60]}
    ]

for dic in data:
    avg = sum(dic["Marks"])//3
    if avg >90:
        grade = "A"
    elif avg >80:
        grade="B+"
    elif avg >70:
        grade = "B"
    elif avg > 60:
        grade = "C"
    elif avg>50:
        grade = "D"
    elif avg > 40:
        grade = "E"
    else:
        grade="F"
    print("id",dic.get("id"),"Name",dic.get("Name"),"Average",avg,"Result",grade)
    
