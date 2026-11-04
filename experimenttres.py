def ticket_price(aantal: int) -> int:
    if aantal < 5:
        return aantal * 10
    else:
        return ticket_price * 8
    
    

if __name__ == '__main__':
    tickets = int(input("Hoeveel tickets wilt ge kopen?"))
    print("Dit is hoeveel je moet betalen:")
    print(ticket_price(tickets))