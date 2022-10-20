from HashTable import HashTable
from ST import SymbolTable

def assertAdd():
    st = SymbolTable(10)
    st.addSimTable(1,10)
    st.addSimTable(3,"asd")
    st.addSimTable("123",12)
    st.addSimTable("a","b")

    assert st.hasIdentifier(6) == None
    assert st.hasIdentifier(1) == 10
    assert st.hasIdentifier(3) == "asd"
    assert st.hasIdentifier("a") == "b"

def assertEdit():
    st = SymbolTable(10)
    st.addSimTable(1,10)
    st.addSimTable(1,15)

    st.addSimTable(2,"a")
    st.addSimTable(2,1)

    assert st.hasIdentifier(1) == 15
    assert st.hasIdentifier(2) == 1

def assertDelete():
    st = SymbolTable(10)
    st.addSimTable(1,10)
    st.addSimTable("a","b")

    assert st.hasIdentifier(1) == 10
    st.deleteIdentifier(1)
    assert st.hasIdentifier(1) == None

    st.deleteIdentifier("a")
    assert st.hasIdentifier("a") == None

if __name__ == '__main__':
    assertAdd()
    assertEdit()
    assertDelete()

