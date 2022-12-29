from Employee.Creators.CreatorRegularEmployee import CreatorRegularEmployee


def test_creator_regular_employee():
    employee = CreatorRegularEmployee('Diego',{}).factory_method()
    assert employee.getName()=='Diego'
    assert (employee.getSchedule)==0