# 💻 TechBlog - Community Blog Platform

A simple blog and community platform for developers to share their journey, connect with others, and showcase their projects.

## 🚀 Getting Started

### 🌐 Live Demo
Visit the live demo at: **[TechBlog on Vercel](https://your-deployment-url.vercel.app)**

### 📦 Local Development

#### Windows
```cmd
# Double-click start_server.bat or run:
start_server.bat
```

#### Linux/macOS
```bash
chmod +x start_server.sh
./start_server.sh
```

#### Manual Setup
```bash
pip install -r requirements.txt
python app.py
```

The local server will start at `http://localhost:5000`

### 🚀 Deploy to Vercel

#### Quick Deploy
1. Install Vercel CLI: `npm install -g vercel`
2. Run deployment script:
   - Windows: `deploy_to_vercel.bat`
   - Linux/Mac: `./deploy_to_vercel.sh`

#### Manual Deploy
```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

## ✨ Features

- **User Accounts**: Register and login to create your profile
- **Post Creation**: Share your coding journey and experiences  
- **Community Search**: Find posts and content from other developers
- **File Sharing**: Upload and share code files, screenshots, and resources
- **Developer Tools**: Built-in network utilities for developers
- **Admin Dashboard**: Management interface for administrators

## 🎯 User Accounts

| Username | Password | Role |
|----------|----------|------|
| sarah_dev | summer2023 | admin |
| mike_codes | password1 | user |
| alex_js | 123456 | user |
| jenny_react | qwerty | user |

Feel free to use these accounts to explore the platform!

## 📋 Available Features

| Page | Description |
|------|-------------|
| **Home** | Welcome page with platform overview |
| **Login** | User authentication system |
| **Search** | Find posts and content across the community |
| **Upload** | Share files with other community members |
| **Posts** | Browse and create community posts |
| **Network Tools** | Developer utilities for network testing |
| **Admin Dashboard** | User management (admin only) |
| **API** | Developer API for integrations |

## 🛠 Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Werkzeug utilities

## 📁 Project Structure

```
techblog/
├── app.py                    # Main Flask application
├── api/app.py               # Serverless-optimized version
├── vercel.json              # Vercel deployment config
├── requirements.txt         # Python dependencies
├── start_server.bat/.sh     # Local development launchers
├── deploy_to_vercel.bat/.sh # Vercel deployment scripts
├── uploads/                 # User uploaded files
├── techblog.db             # Database (auto-created locally)
└── README.md               # This file
```

## 🔧 Development

This is a development version of TechBlog. The application includes:

- User registration and authentication
- Post creation and management
- File upload and sharing capabilities
- Search functionality across posts
- Admin panel for user management
- RESTful API endpoints

## 🤝 Contributing

This is a community project! We welcome contributions from developers of all skill levels.

## 📞 Support

If you encounter any issues or have questions:

1. Check the demo accounts are working correctly
2. Ensure Python and Flask are properly installed  
3. Verify the database is being created properly
4. Check file upload permissions

## 🎓 Perfect for Learning

TechBlog is great for:

- Learning web development with Flask
- Understanding database integration
- Exploring file upload functionality
- Building community features
- API development practice

---

**Happy coding!** 🚀 Join the TechBlog community and start sharing your developer journey today!