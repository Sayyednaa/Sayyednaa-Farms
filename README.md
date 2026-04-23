# 🌾 Sayyednaa Farms - Premium Organic Platform

[![Django](https://img.shields.io/badge/Framework-Django%204.2-092e20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Design](https://img.shields.io/badge/Design-Obsidian%20%26%20Emerald-10B981?style=for-the-badge)](https://sayyednaafarms.com)
[![Platform](https://img.shields.io/badge/Platform-Mobile--First-6366F1?style=for-the-badge)](https://sayyednaafarms.com)

A high-performance, mobile-first Farm Management and E-commerce platform designed for **Sayyednaa Farms**. This platform bridges the gap between traditional sustainable agriculture and modern digital commerce, specializing in aquaculture, premium livestock, and organic horticulture.

---

## ✨ Key Features

### 📱 Premium User Experience
- **Obsidian & Emerald UI**: A custom-built design system featuring deep dark modes, glassmorphism, and vibrant emerald accents.
- **Mobile-First Architecture**: Includes a fixed bottom navigation bar and a responsive hamburger drawer for seamless browsing on any device.
- **Dynamic Interactivity**: Custom JavaScript toast notifications, smooth scroll animations, and a high-performance gallery lightbox.

### 🛒 Farm-to-Table Commerce
- **Smart Cart System**: Real-time quantity management (increment/decrement) with a live cart count badge in the navigation.
- **Collection-Only Model**: Integrated "Farmhouse Collection" policy ensuring zero-carbon delivery and maximum freshness.
- **Priority Booking**: Automated logic that prioritizes online bookings over walk-in customers.
- **Secure Checkout**: Simplified, mobile-optimized checkout flow with automated order confirmation.

### 🔐 Advanced Farm Management (Admin)
- **Unified Staff Dashboard**: Real-time statistics on revenue, livestock health, and plantation growth.
- **Modular Management**: Dedicated interfaces for:
  - **Livestock**: Health tracking and inventory management.
  - **Crops**: Plantation mapping and harvest forecasting.
  - **Inventory**: Stock tracking with automated low-stock alerts.
  - **Shop**: Product management and order fulfillment.

---

## 🛠️ Technology Stack

- **Backend**: Python / Django 4.2
- **Frontend**: Vanilla HTML5, CSS3 (Custom Design System), Modern JavaScript (ES6+)
- **Database**: SQLite (Development) / PostgreSQL (Production ready)
- **Styling**: Pure CSS (No external frameworks for maximum performance and unique aesthetics)
- **Icons**: FontAwesome 6 / Google Fonts (Outfit & Inter)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Pip (Python Package Manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sayyednaa-farms.git
   cd sayyednaa-farms
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the server**
   ```bash
   python manage.py runserver
   ```

Access the platform at `http://127.0.0.1:8000`.

---

## 📸 Design Philosophy

The project follows a **Glassmorphism** aesthetic, utilizing:
- `backdrop-filter: blur(12px)` for premium depth.
- `linear-gradient` overlays for high-impact visual storytelling.
- `1280px` max-width container for desktop clarity.
- `70px` navigation safety zones for mobile accessibility.

---

## 👨‍🌾 Credits

- **Sayyed Nawab Abdul Adil**: Founder & Veterinary Specialist
- **Sayyed Nawab Abdul Ali**: Co-Founder & Software Engineer

---

© 2026 Sayyednaa Farms. Built with ❤️ for sustainable living.
