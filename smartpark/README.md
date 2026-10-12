# SmartPark — Free Smart Parking System

## Setup & Run

### 1. Install Python dependencies
```
pip install django
```

### 2. Apply database migrations
```
python manage.py migrate
```

### 3. Seed the parking slots (450 slots: 3 entrances × 3 levels × 50 slots)
```
python manage.py seed_slots
```

### 4. Create an admin user (optional)
```
python manage.py createsuperuser
```

### 5. Start the development server
```
python manage.py runserver
```

### 6. Open in browser
- **App**: http://127.0.0.1:8000/
- **Admin panel**: http://127.0.0.1:8000/admin/ (username: admin, password: set by you)

---

## How to Use

### Entering the parking lot
1. Click **ENTRANCE** on the welcome page
2. Choose an entrance: **South**, **East**, or **North**
3. Choose a parking **level** (1, 2, or 3)
4. The slot grid shows **green = available**, **red = occupied**
5. Tap any green slot to select it, then click **Confirm & Get Receipt**
6. Your receipt displays your **slot number** and **verification code**
7. Click **Open Gate & Enter** — boom gate and spikes open simultaneously
8. Drive to your assigned slot

### Exiting the parking lot
1. Click **EXIT** (top right or home page)
2. Enter your **slot number** (e.g. `S-L1-012`)
3. Enter your **verification code** (e.g. `A1B2C3`)
4. Click **Verify & Exit** — system validates, releases your slot, opens the gate
5. You are redirected to the Thank You page, then back to home after 3 seconds

---

## Slot ID Format
`[Entrance Initial]-L[Level]-[Number]`  
Examples: `S-L1-001`, `E-L2-025`, `N-L3-050`

## Project Structure
```
smartpark/
├── manage.py
├── db.sqlite3
├── smartpark/          # Project settings
│   ├── settings.py
│   └── urls.py
└── parking/            # Main app
    ├── models.py       # ParkingSlot model
    ├── views.py        # All page logic
    ├── urls.py         # URL routing
    ├── admin.py        # Django admin
    ├── management/commands/seed_slots.py
    └── templates/parking/
        ├── base.html
        ├── welcome.html
        ├── entrance.html
        ├── level.html
        ├── slots.html
        ├── receipt.html
        ├── parked.html
        ├── exit.html
        └── thankyou.html
```
