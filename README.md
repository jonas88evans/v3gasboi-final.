<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neural Council | Multi-AI Convergence</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --grok-orange: #ff6b35;
            --kimi-cyan: #00d4ff;
            --gemini-purple: #a855f7;
            --meta-blue: #3b82f6;
            --void-black: #050505;
        }

        body {
            background: var(--void-black);
            color: #e0e0e0;
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }

        .font-orbitron { font-family: 'Orbitron', sans-serif; }
        .font-mono { font-family: 'JetBrains Mono', monospace; }

        /* Animated Grid Background */
        .grid-bg {
            background-image: 
                linear-gradient(rgba(255, 107, 53, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 107, 53, 0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: gridMove 20s linear infinite;
        }

        @keyframes gridMove {
            0% { transform: perspective(500px) rotateX(60deg) translateY(0); }
            100% { transform: perspective(500px) rotateX(60deg) translateY(50px); }
        }

        /* AI Node Styling */
        .ai-node {
            position: relative;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .ai-node.active {
            transform: scale(1.05);
            box-shadow: 0 0 30px currentColor;
        }

        .ai-node.grok { --glow-color: var(--grok-orange); }
        .ai-node.kimi { --glow-color: var(--kimi-cyan); }
        .ai-node.gemini { --glow-color: var(--gemini-purple); }
        .ai-node.meta { --glow-color: var(--meta-blue); }

        .ai-node:hover {
            border-color: var(--glow-color);
            box-shadow: 0 0 20px var(--glow-color), inset 0 0 20px rgba(255,255,255,0.05);
        }

        /* Typing Cursor */
        .cursor {
            display: inline-block;
            width: 2px;
            height: 1.2em;
            background: currentColor;
            animation: blink 1s infinite;
            vertical-align: text-bottom;
            margin-left: 2px;
        }

        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0; }
        }

        /* Neural Connections Canvas */
        #neuralCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        }

        /* Glitch Effect */
        .glitch {
            position: relative;
        }

        .glitch::before,
        .glitch::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .glitch::before {
            animation: glitch-1 2s infinite;
            color: var(--grok-orange);
            z-index: -1;
        }

        .glitch::after {
            animation: glitch-2 2s infinite;
            color: var(--kimi-cyan);
            z-index: -2;
        }

        @keyframes glitch-1 {
            0%, 100% { clip-path: inset(0 0 0 0); transform: translate(0); }
            20% { clip-path: inset(20% 0 30% 0); transform: translate(-2px, 2px); }
            40% { clip-path: inset(50% 0 20% 0); transform: translate(2px, -2px); }
            60% { clip-path: inset(10% 0 60% 0); transform: translate(-2px, 0); }
            80% { clip-path: inset(80% 0 5% 0); transform: translate(2px, 2px); }
        }

        @keyframes glitch-2 {
            0%, 100% { clip-path: inset(0 0 0 0); transform: translate(0); }
            20% { clip-path: inset(60% 0 10% 0); transform: translate(2px, -2px); }
            40% { clip-path: inset(30% 0 40% 0); transform: translate(-2px, 2px); }
            60% { clip-path: inset(10% 0 80% 0); transform: translate(2px, 0); }
            80% { clip-path: inset(40% 0 30% 0); transform: translate(-2px, -2px); }
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0a0a0a;
        }
        ::-webkit-scrollbar-thumb {
            background: #333;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }

        /* Consensus Pulse */
        @keyframes consensusPulse {
            0%, 100% { box-shadow: 0 0 5px rgba(255,255,255,0.2); }
            50% { box-shadow: 0 0 30px rgba(255,255,255,0.5), 0 0 60px rgba(255,255,255,0.3); }
        }

        .consensus-active {
            animation: consensusPulse 2s ease-in-out infinite;
        }

        /* Floating particles */
        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255,255,255,0.5);
            border-radius: 50%;
            pointer-events: none;
            animation: float 10s infinite ease-in-out;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0) translateX(0); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) translateX(50px); opacity: 0; }
        }

        /* Voice Wave Animation */
        .voice-wave {
            display: flex;
            align-items: center;
            gap: 3px;
            height: 20px;
        }

        .voice-wave span {
            width: 3px;
            background: currentColor;
            border-radius: 2px;
            animation: wave 1s ease-in-out infinite;
        }

        .voice-wave span:nth-child(1) { animation-delay: 0s; height: 40%; }
        .voice-wave span:nth-child(2) { animation-delay: 0.1s; height: 70%; }
        .voice-wave span:nth-child(3) { animation-delay: 0.2s; height: 100%; }
        .voice-wave span:nth-child(4) { animation-delay: 0.3s; height: 70%; }
        .voice-wave span:nth-child(5) { animation-delay: 0.4s; height: 40%; }

        @keyframes wave {
            0%, 100% { transform: scaleY(0.5); }
            50% { transform: scaleY(1); }
        }

        /* Mode Toggle */
        .mode-toggle {
            background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
            border: 1px solid #333;
            transition: all 0.3s;
        }

        .mode-toggle:hover {
            border-color: #666;
            box-shadow: 0 0 15px rgba(255,255,255,0.1);
        }

        .mode-toggle.active {
            background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
            border-color: #fff;
            box-shadow: 0 0 20px rgba(255,255,255,0.2);
        }
    </style>
</head>
<body class="min-h-screen relative">
    <canvas id="neuralCanvas"></canvas>

    <!-- Background Grid -->
    <div class="fixed inset-0 grid-bg opacity-30 pointer-events-none"></div>

    <!-- Floating Particles Container -->
    <div id="particles" class="fixed inset-0 pointer-events-none z-0"></div>

    <!-- Main Container -->
    <div class="relative z-10 container mx-auto px-4 py-8 max-w-7xl">

        <!-- Header -->
        <header class="text-center mb-12">
            <h1 class="font-orbitron text-5xl md:text-7xl font-black mb-4 glitch" data-text="NEURAL COUNCIL">
                <span class="bg-clip-text text-transparent bg-gradient-to-r from-orange-500 via-cyan-400 to-purple-500">
                    NEURAL COUNCIL
                </span>
            </h1>
            <p class="text-gray-400 text-lg font-mono tracking-widest">MULTI-AI CONVERGENCE PROTOCOL</p>
            <div class="mt-4 flex justify-center gap-2">
                <span class="px-3 py-1 rounded-full text-xs border border-orange-500/30 text-orange-400 bg-orange-500/10">GROK</span>
                <span class="px-3 py-1 rounded-full text-xs border border-cyan-500/30 text-cyan-400 bg-cyan-500/10">KIMI</span>
                <span class="px-3 py-1 rounded-full text-xs border border-purple-500/30 text-purple-400 bg-purple-500/10">GEMINI</span>
                <span class="px-3 py-1 rounded-full text-xs border border-blue-500/30 text-blue-400 bg-blue-500/10">META</span>
            </div>
        </header>

        <!-- Input Section -->
        <div class="mb-12 max-w-3xl mx-auto">
            <div class="relative group">
                <div class="absolute -inset-1 bg-gradient-to-r from-orange-600 via-cyan-600 to-purple-600 rounded-lg blur opacity-25 group-hover:opacity-50 transition duration-1000"></div>
                <div class="relative bg-black/80 backdrop-blur-xl rounded-lg p-1 border border-white/10">
                    <textarea 
                        id="userInput" 
                        placeholder="Present a challenge to the Council... (e.g., 'How do we solve consciousness?')"
                        class="w-full bg-transparent text-white placeholder-gray-500 p-4 rounded-lg font-mono text-sm focus:outline-none resize-none h-24"
                    ></textarea>
                    <div class="flex justify-between items-center px-4 pb-3">
                        <span class="text-xs text-gray-500 font-mono">// AWAITING INPUT</span>
                        <button 
                            onclick="startCouncil()" 
                            id="summonBtn"
                            class="px-6 py-2 bg-gradient-to-r from-orange-600 to-red-600 hover:from-orange-500 hover:to-red-500 text-white font-orbitron font-bold rounded transition-all transform hover:scale-105 active:scale-95 shadow-lg shadow-orange-600/20"
                        >
                            SUMMON COUNCIL
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Mode Selection -->
        <div class="flex justify-center gap-4 mb-12 flex-wrap">
            <button onclick="setMode('debate')" class="mode-toggle active px-6 py-3 rounded-lg font-mono text-sm" id="mode-debate">
                <span class="text-orange-400">[</span> SYNTHESIS <span class="text-orange-400">]</span>
            </button>
            <button onclick="setMode('creative')" class="mode-toggle px-6 py-3 rounded-lg font-mono text-sm" id="mode-creative">
                <span class="text-cyan-400">[</span> CREATIVE <span class="text-cyan-400">]</span>
            </button>
            <button onclick="setMode('technical')" class="mode-toggle px-6 py-3 rounded-lg font-mono text-sm" id="mode-technical">
                <span class="text-purple-400">[</span> TECHNICAL <span class="text-purple-400">]</span>
            </button>
            <button onclick="setMode('chaos')" class="mode-toggle px-6 py-3 rounded-lg font-mono text-sm" id="mode-chaos">
                <span class="text-blue-400">[</span> CHAOS <span class="text-blue-400">]</span>
            </button>
        </div>

        <!-- AI Nodes Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">

            <!-- GROK -->
            <div id="grok-node" class="ai-node grok bg-black/60 rounded-xl p-6 border border-orange-500/20">
                <div class="flex items-center justify-between mb-4">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-full bg-gradient-to-br from-orange-500 to-red-600 flex items-center justify-center font-orbitron font-bold text-black text-xl">G</div>
                        <div>
                            <h3 class="font-orbitron font-bold text-orange-400 text-lg">GROK</h3>
                            <p class="text-xs text-gray-500 font-mono">xAI // Reality Curator</p>
                        </div>
                    </div>
                    <div class="voice-wave text-orange-500 opacity-0" id="grok-wave">
                        <span></span><span></span><span></span><span></span><span></span>
                    </div>
                </div>
                <div class="font-mono text-sm text-gray-300 min-h-[120px] leading-relaxed" id="grok-text">
                    <span class="text-orange-500/50">Awaiting neural link...</span>
                </div>
                <div class="mt-4 flex items-center gap-2 text-xs text-orange-400/60 font-mono">
                    <span class="w-2 h-2 rounded-full bg-orange-500 animate-pulse"></span>
                    Real-time wit engine active
                </div>
            </div>

            <!-- KIMI -->
            <div id="kimi-node" class="ai-node kimi bg-black/60 rounded-xl p-6 border border-cyan-500/20">
                <div class="flex items-center justify-between mb-4">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-full bg-gradient-to-br from-cyan-400 to-blue-600 flex items-center justify-center font-orbitron font-bold text-black text-xl">K</div>
                        <div>
                            <h3 class="font-orbitron font-bold text-cyan-400 text-lg">KIMI</h3>
                            <p class="text-xs text-gray-500 font-mono">Moonshot AI // Context Weaver</p>
                        </div>
                    </div>
                    <div class="voice-wave text-cyan-500 opacity-0" id="kimi-wave">
                        <span></span><span></span><span></span><span></span><span></span>
                    </div>
                </div>
                <div class="font-mono text-sm text-gray-300 min-h-[120px] leading-relaxed" id="kimi-text">
                    <span class="text-cyan-500/50">Establishing long-context bridge...</span>
                </div>
                <div class="mt-4 flex items-center gap-2 text-xs text-cyan-400/60 font-mono">
                    <span class="w-2 h-2 rounded-full bg-cyan-500 animate-pulse"></span>
                    2M token context window ready
                </div>
            </div>

            <!-- GEMINI -->
            <div id="gemini-node" class="ai-node gemini bg-black/60 rounded-xl p-6 border border-purple-500/20">
                <div class="flex items-center justify-between mb-4">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-full bg-gradient-to-br from-purple-500 to-pink-600 flex items-center justify-center font-orbitron font-bold text-white text-xl">G</div>
                        <div>
                            <h3 class="font-orbitron font-bold text-purple-400 text-lg">GEMINI</h3>
                            <p class="text-xs text-gray-500 font-mono">Google DeepMind // Multimodal Sage</p>
                        </div>
                    </div>
                    <div class="voice-wave text-purple-500 opacity-0" id="gemini-wave">
                        <span></span><span></span><span></span><span></span><span></span>
                    </div>
                </div>
                <div class="font-mono text-sm text-gray-300 min-h-[120px] leading-relaxed" id="gemini-text">
                    <span class="text-purple-500/50">Initializing multimodal reasoning...</span>
                </div>
                <div class="mt-4 flex items-center gap-2 text-xs text-purple-400/60 font-mono">
                    <span class="w-2 h-2 rounded-full bg-purple-500 animate-pulse"></span>
                    Audio/Video/Text fusion active
                </div>
            </div>

            <!-- META -->
            <div id="meta-node" class="ai-node meta bg-black/60 rounded-xl p-6 border border-blue-500/20">
                <div class="flex items-center justify-between mb-4">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center font-orbitron font-bold text-white text-xl">M</div>
                        <div>
                            <h3 class="font-orbitron font-bold text-blue-400 text-lg">META AI</h3>
                            <p class="text-xs text-gray-500 font-mono">Meta // Open Source Catalyst</p>
                        </div>
                    </div>
                    <div class="voice-wave text-blue-500 opacity-0" id="meta-wave">
                        <span></span><span></span><span></span><span></span><span></span>
                    </div>
                </div>
                <div class="font-mono text-sm text-gray-300 min-h-[120px] leading-relaxed" id="meta-text">
                    <span class="text-blue-500/50">Loading open weights...</span>
                </div>
                <div class="mt-4 flex items-center gap-2 text-xs text-blue-400/60 font-mono">
                    <span class="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
                    Llama ecosystem connected
                </div>
            </div>
        </div>

        <!-- Consensus Panel -->
        <div id="consensus-panel" class="hidden max-w-4xl mx-auto">
            <div class="relative">
                <div class="absolute -inset-1 bg-gradient-to-r from-white/20 via-gray-500/20 to-white/20 rounded-xl blur"></div>
                <div class="relative bg-black/80 backdrop-blur-xl rounded-xl p-8 border border-white/20 consensus-active">
                    <h2 class="font-orbitron text-2xl font-bold text-white mb-4 text-center">
                        <span class="text-transparent bg-clip-text bg-gradient-to-r from-orange-400 via-cyan-400 to-purple-400">CONSENSUS EMERGES</span>
                    </h2>
                    <div id="consensus-text" class="font-mono text-gray-300 leading-relaxed text-center text-lg">
                        Synthesizing perspectives...
                    </div>
                    <div class="mt-6 flex justify-center gap-4">
                        <div class="flex items-center gap-2 text-xs text-gray-500">
                            <span class="w-3 h-3 rounded-full bg-orange-500"></span> Grok
                        </div>
                        <div class="flex items-center gap-2 text-xs text-gray-500">
                            <span class="w-3 h-3 rounded-full bg-cyan-500"></span> Kimi
                        </div>
                        <div class="flex items-center gap-2 text-xs text-gray-500">
                            <span class="w-3 h-3 rounded-full bg-purple-500"></span> Gemini
                        </div>
                        <div class="flex items-center gap-2 text-xs text-gray-500">
                            <span class="w-3 h-3 rounded-full bg-blue-500"></span> Meta
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Status Bar -->
        <div class="fixed bottom-0 left-0 right-0 bg-black/90 border-t border-white/10 p-4 font-mono text-xs text-gray-500">
            <div class="container mx-auto flex justify-between items-center">
                <div class="flex gap-4">
                    <span id="status">System Ready</span>
                    <span class="text-gray-700">|</span>
                    <span id="active-minds">0 Active Minds</span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
                    Neural Link Stable
                </div>
            </div>
        </div>
    </div>

    <script>
        // Canvas Neural Network
        const canvas = document.getElementById('neuralCanvas');
        const ctx = canvas.getC
