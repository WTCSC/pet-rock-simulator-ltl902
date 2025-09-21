# Virtual Pet Rock Game

A simple Python terminal game where you take care of your very own pet rock!  
Keep it **happy**, **clean**, and **fed** – or risk losing your only friend.  

---

## Features
- Name your pet rock.
- Keep track of:
  - **Happiness**
  - **Cleanliness**
  - **Hunger**
- Multiple actions:
  - Play with your rock
  - Clean your rock
  - Feed your rock
  - Stare at your rock (secret choices)
  - Put sunglasses on your rock
- Dynamic moods (`o(＾▽＾)o`, `(•︵•)`, `(ಥ﹏ಥ)`)
- ASCII art animations
- Multiple possible endings (some darkly funny).

---

## Requirements
- Python **3.8+**
- No external libraries required (uses only built-in modules: `time` and `sys`).

---

## How to Run
1. Clone this repository or copy the script into a `.py` file (e.g., `pet_rock.py`).
2. Run the script in your terminal:

   ```bash
   python pet_rock.py
   ```

3. Follow the prompts to name your pet rock and interact with it.

---

## Gameplay
- Your pet rock starts with balanced stats:
  - Happiness: 5  
  - Cleanliness: 5  
  - Hunger: 5  
- Each turn, stats decrease (or increase, in the case of hunger).
- Choose an action each round to keep your rock alive and happy.  

### Possible Actions:
1. **Play** → increases happiness.  
2. **Clean** → increases cleanliness (but don’t look away during the bath).  
3. **Feed** → decreases hunger (don’t overfeed or underfeed).  
4. **Stare** → mysterious choices (hammer or strange liquid).  
5. **Glasses** → give your rock sunglasses.  

---

## Game Over Conditions
- Happiness ≤ 0  
- Cleanliness ≤ 0  
- Hunger ≥ 10  
- Special events (erosion, cracking, melting, implosion, etc.)  

When your rock is gone…  
> "Your only friend is gone. You feel sad and lonely. GAME OVER."  

---

## Function Flowchart

```mermaid
flowchart

    A[main()] --> B[init_pet()]
    A --> C[game_loop()]
    
    C --> D[display_status()]
    C --> E[get_player_choice()]
    C --> F[apply_choice()]
    C --> G[update_stats()]
    C --> H[check_game_over()]
    
    F --> F1[play_with_pet()]
    F --> F2[clean_pet()]
    F --> F3[feed_pet()]
    F --> F4[stare_at_pet()]
    F --> F5[put_glasses_on_pet()]
    
    H -->|If dead| [game_over()]
    H -->|Else| C
```
