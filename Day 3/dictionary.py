                                        #dictioanry
users = {
    "names": ["Abdul", "Ali", "Ahmad"],
    "ages": [26, 24, 28],
    "cities": ["Lahore", "Karachi", "Islamabad"]
}
print(users["names"])
print(users["ages"])
print(users["cities"])
users["names"].append("konan")
users["ages"].append(29)
users["cities"].append("Lahore")
print(users)
users["names"][0] = "Abdul rehman"
print(users)
                        #function to get users from lahore
def get_lahore_users(users):
    lah_users = []

    for i in range(len(users["cities"])):
        if users["cities"][i] == "Lahore":
            lah_users.append(users["names"][i])

    return lah_users
print(get_lahore_users(users))  