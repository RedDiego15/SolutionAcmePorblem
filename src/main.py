from Employe.Creators.CreatorRegularEmployee import CreatorRegularEmployee


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    
    employee = CreatorRegularEmployee('Diego',{}).factory_method()
    print(employee.getName())
    print(employee.getSchedule())
