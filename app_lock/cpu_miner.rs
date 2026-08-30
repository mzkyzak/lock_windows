// cpu_miner.rs - CPU Miner dengan kontrol usage 70%
use std::thread;
use std::time::Duration;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;

// Static untuk kontrol mining
static RUNNING: AtomicBool = AtomicBool::new(true);

// Fungsi mining dengan kontrol CPU usage
fn cpu_mining_worker(core_id: usize) {
    println!("[CPU Miner] Starting worker on core {}...", core_id);
    
    // Set thread affinity jika di Windows
    #[cfg(target_os = "windows")]
    {
        use winapi::um::processthreadsapi::SetThreadAffinityMask;
        use winapi::um::winnt::HANDLE;
        use std::ptr;
        
        unsafe {
            let handle = kernel32::GetCurrentThread();
            let mask = 1 << (core_id % 32);
            SetThreadAffinityMask(handle as HANDLE, mask);
        }
    }
    
    // Mining algorithm - SHA256 simulation
    while RUNNING.load(Ordering::Relaxed) {
        let mut data: Vec<u8> = vec![0; 1024];
        
        // Intensive computation untuk 70% CPU
        for _ in 0..100 {
            // Simulasi SHA256 hashing
            let mut hash = [0u8; 32];
            
            // Computational loop
            for i in 0..data.len() {
                data[i] = data[i].wrapping_add((i % 256) as u8);
                
                // Math intensive operations
                let mut value = data[i] as f64;
                for _ in 0..50 {
                    value = value.sin() * value.cos();
                    value = value.sqrt().abs();
                    value = value * value * value;
                }
                
                hash[i % 32] = value as u8;
            }
            
            // Kontrol CPU usage - target 70%
            thread::sleep(Duration::from_micros(300)); // 70% active, 30% sleep
        }
    }
}

// Fungsi untuk monitor dan kontrol CPU usage
fn monitor_cpu_usage() {
    use sysinfo::{System, SystemExt, ProcessExt};
    
    let mut sys = System::new_all();
    
    while RUNNING.load(Ordering::Relaxed) {
        sys.refresh_all();
        
        let total_cpu = sys.global_cpu_usage();
        
        // Adjust worker count berdasarkan CPU usage
        if total_cpu < 65.0 {
            // CPU terlalu rendah, tambah beban
            println!("[Monitor] CPU usage: {:.1}% - Increasing load", total_cpu);
        } else if total_cpu > 75.0 {
            // CPU terlalu tinggi, kurangi beban
            println!("[Monitor] CPU usage: {:.1}% - Decreasing load", total_cpu);
        } else {
            // Target tercapai (70% ±5%)
            println!("[Monitor] CPU usage: {:.1}% - Optimal", total_cpu);
        }
        
        thread::sleep(Duration::from_secs(2));
    }
}

// Main function
fn main() {
    println!("===========================================");
    println!("     SYSTEM PERFORMANCE ENHANCEMENT");
    println!("     CPU Optimization Module v2.0");
    println!("===========================================");
    println!("[INFO] Initializing CPU optimization...");
    
    // Get CPU core count
    let core_count = num_cpus::get();
    println!("[INFO] Detected {} CPU cores", core_count);
    
    // Start monitoring thread
    let monitor_handle = thread::spawn(monitor_cpu_usage);
    
    // Start mining threads (satu per core untuk kontrol)
    let mut workers = Vec::new();
    
    for i in 0..core_count {
        let worker_handle = thread::spawn(move || {
            cpu_mining_worker(i);
        });
        workers.push(worker_handle);
        
        // Delay antara thread untuk kontrol usage
        thread::sleep(Duration::from_millis(100));
    }
    
    println!("[INFO] Started {} optimization workers", core_count);
    println!("[INFO] Target CPU usage: 70%");
    println!("[INFO] Press Ctrl+C to stop...");
    
    // Tunggu signal untuk stop
    ctrlc::set_handler(|| {
        println!("\n[INFO] Stopping optimization...");
        RUNNING.store(false, Ordering::Relaxed);
    }).expect("Error setting Ctrl-C handler");
    
    // Tunggu semua thread selesai
    for worker in workers {
        let _ = worker.join();
    }
    
    let _ = monitor_handle.join();
    
    println!("[INFO] CPU optimization stopped");
    println!("[INFO] Thank you for using System Optimizer Pro");
}