import re

with open("/Users/eduardoteixeira/Downloads/site/generated-page-4.index.html", "r") as f:
    content = f.read()

# 1. Video Safari Bug
content = content.replace('autoplay loop muted playsinline webkit-playsinline preload="auto"', 'playsinline webkit-playsinline muted autoplay loop')
content = content.replace('autoplay loop muted playsinline webkit-playsinline class="absolute', 'playsinline webkit-playsinline muted autoplay loop class="absolute')

# 2. Carousel Mobile Layout
content = content.replace('w-[85vw] md:w-[900px] flex-none grid grid-cols-1 md:grid-cols-2 gap-4 snap-center', 'w-[90vw] md:w-[900px] max-w-none flex-none grid grid-cols-2 gap-2 md:gap-6 snap-center')
content = content.replace('bg-[#0a0a0a] rounded-2xl border border-white/10 p-8 relative flex flex-col shadow-[0_0_20px_rgba(0,0,0,0.5)]', 'bg-[#0a0a0a] rounded-2xl border border-white/10 p-3 md:p-8 relative flex flex-col shadow-[0_0_20px_rgba(0,0,0,0.5)]')
content = content.replace('text-2xl font-semibold text-white mb-6', 'text-sm md:text-2xl font-semibold text-white mb-2 md:mb-6 leading-tight')
content = content.replace('flex items-center gap-3 border border-white/10 rounded-2xl p-4 bg-white/5 w-full mb-3', 'flex items-center gap-1.5 md:gap-3 border border-white/10 rounded-xl md:rounded-2xl p-2 md:p-4 bg-white/5 w-full mb-1.5 md:mb-3')
content = content.replace('w-8 h-8 rounded-lg bg-white/10 flex items-center justify-center shrink-0 border border-white/5', 'w-5 h-5 md:w-8 md:h-8 rounded-lg bg-white/10 flex items-center justify-center shrink-0 border border-white/5')
content = content.replace('text-[#FF9EB5] text-sm', 'text-[#FF9EB5] text-[10px] md:text-sm')
content = content.replace('text-sm text-gray-300 font-medium', 'text-[10px] md:text-base text-gray-300 font-medium leading-tight')
content = content.replace('inline-flex items-center px-3 py-1 rounded-full border border-white/10 bg-white/5 text-[10px] text-gray-400 font-semibold tracking-widest uppercase mb-6 w-max', 'inline-flex items-center px-2 py-0.5 md:px-3 md:py-1 rounded-full border border-white/10 bg-white/5 text-[8px] md:text-[10px] text-gray-400 font-semibold tracking-widest uppercase mb-2 md:mb-6 w-max')
content = content.replace('bg-[#0a0a0a] rounded-2xl border border-white/10 overflow-hidden relative aspect-square md:aspect-auto shadow-[0_0_20px_rgba(0,0,0,0.5)]', 'bg-[#0a0a0a] rounded-2xl border border-white/10 overflow-hidden relative shadow-[0_0_20px_rgba(0,0,0,0.5)] h-full min-h-[200px]')
content = content.replace('mb-12 flex-1', 'mb-2 md:mb-12 flex-1')


# 3. Global Whitespace Mobile Tightening
content = content.replace('pt-40 pr-6 pb-20 pl-6', 'pt-28 md:pt-40 pr-6 pb-12 md:pb-20 pl-6')
content = content.replace('mt-20 relative', 'mt-10 md:mt-20 relative')
content = content.replace('py-24 bg-', 'py-12 md:py-24 bg-')
content = content.replace('py-20 bg-', 'py-12 md:py-20 bg-')
content = content.replace('py-20 px-6', 'py-12 md:py-20 px-6')
content = content.replace('py-24 text-center', 'py-12 md:py-24 text-center')
content = content.replace('py-24 relative', 'py-12 md:py-24 relative')
content = content.replace('gap-20 items-center', 'gap-10 md:gap-20 items-center')
content = content.replace('mb-20', 'mb-10 md:mb-20')

with open("/Users/eduardoteixeira/Downloads/site/generated-page-4.index.html", "w") as f:
    f.write(content)

