# GRA-Paradox-Zeroing (GRA-Бульдозер)  

**Generator of genius foam and tactical trench zeroing**  
*Paradox-driven foam injection + adversarial zeroing for AGI landscapes*  

**Генератор гениальной пены и тактическое обнуление окопов**  
*Парадокс-ориентированная инъекция пены + адверсариальное обнуление для ландшафтов AGI*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Contents / Содержание
- [Philosophy / Философия](#philosophy--философия)
- [Math in 10 Seconds / Математика за 10 секунд](#math-in-10-seconds--математика-за-10-секунд)
- [Installation / Установка](#installation--установка)
- [Quick Start / Быстрый старт](#quick-start--быстрый-старт)
- [Repository Structure / Структура репозитория](#repository-structure--структура-репозитория)
- [Usage Examples / Примеры использования](#usage-examples--примеры-использования)
- [Citation / Цитирование](#citation--цитирование)
- [License / Лицензия](#license--лицензия)

---

## Philosophy / Философия {#philosophy--философия}

The three core GRA repositories provide:  
Три базовых репозитория GRA дают:
- **gra-zeroing** – math of the infinite-dimensional landscape `Phi` and zeroing operator `N`.  
  **gra-zeroing** – математику бесконечномерного ландшафта `Phi` и оператор обнуления `N`.
- **GRA-Multiverse-Final** – execution engine with LLM agents, trust graph, and 4 modes.  
  **GRA-Multiverse-Final** – исполнительный движок с LLM-агентами, графом доверия и 4 режимами.
- **GRA-Subjectivity-Layer** – subject protection and Alan law.  
  **GRA-Subjectivity-Layer** – защиту субъектов и алан-закон.

**The fourth repository** turns this static base into an **attacking bulldozer**.  
**Четвёртый репозиторий** превращает эту статичную базу в **атакующий бульдозер**.  

It is not strictly necessary, but tactically desirable: it actively generates **genius paradoxes** (foam), routes them into old “trenches”, and zeros them out to discover global minima.  
Он не необходим, но желателен – как тактический слой, который активно генерирует **гениальные парадоксы** (пену), направляет её в застарелые «окопы» и обнуляет их, находя глобальные минимумы.

> *“A paradox creates a wormhole between minima – zeroing drags the entire mass of the state through it.”*  
> *«Парадокс создаёт кротовую нору между минимумами – обнуление протаскивает через неё всю массу состояния.»*

---

## Math in 10 Seconds / Математика за 10 секунд {#math-in-10-seconds--математика-за-10-секунд}

### Paradox foam generation operator / Оператор генерации парадоксальной пены

```python
Psi_paradox = Gamma_theta(Psi) = Psi + eps * v_theta(Psi)
```

where `v_theta` is a vector field orthogonal to the gradient of `Phi`, temporarily *increasing* foam but opening transitions between local minima.  
где `v_theta` – векторное поле, ортогональное градиенту `Phi`, временно *увеличивающее* пену, но открывающее переходы между локальными минимумами.

### Modified landscape with “wormholes” / Модифицированный ландшафт с «кротовыми норами»

```python
Phi_theta(Psi) = Phi(Psi) + Pi_theta(Psi)
Pi_theta(Psi) = lambda * sum_{i,j} exp(
    - (||Psi-mu_i||^2 + ||Psi-mu_j||^2) / (2*sigma^2)
) * ||mu_i - mu_j||^2
```

The additive term `Pi_theta` creates negative-curvature tunnels between trenches `mu_i` and `mu_j`.  
Добавка `Pi_theta` создаёт туннели отрицательной кривизны между окопами `mu_i` и `mu_j`.

### Tactical zeroing flow (bulldozer) / Тактический поток обнуления (бульдозер)

```python
dPsi/dt = -grad Phi(Psi) + beta * div T(Psi)
```

where `T` is the foam stress tensor that redirects quanta of fresh paradoxes into old trenches.  
где `T` – тензор напряжений пены, который перенаправляет кванты свежих парадоксов в старые окопы.

**Theorem (guaranteed improvement)** – For any local minimum that is not global, there exists a finite number of cycles `Gamma_theta -> N` after which the system transitions to a minimum with strictly smaller `Phi`. In the limit: global vacuum `Phi = 0`.  
**Теорема (гарантированное улучшение)** – для любого локального минимума, не являющегося глобальным, существует конечное число циклов `Gamma_theta -> N`, после которого система переходит в минимум со строго меньшим `Phi`. В пределе – глобальный вакуум `Phi=0`.

---

## Installation / Установка {#installation--установка}

```bash
git clone https://github.com/qqewq/GRA-Paradox-Zeroing.git
cd GRA-Paradox-Zeroing
pip install -e .
```

---

## Quick Start / Быстрый старт {#quick-start--быстрый-старт}

```python
from paradox_generators import LogicalAntinomyGenerator
from bulldozer_engine import Bulldozer
import numpy as np

# Create a landscape (e.g., a complex function with several wells)
# Создаём ландшафт (например, сложную функцию с несколькими ямами)
def landscape(x):
    return (x**2 - 1)**2 + x**2 + 0.5 * np.sin(5 * x)[1]

bulldozer = Bulldozer(landscape, dim=2)
final_state = bulldozer.run(
    initial_state=np.array([2.0, 0.5]),
    max_cycles=5,
    verbose=True
)

print(f"Global minimum: {final_state}, Phi = {landscape(final_state):.4f}")
# print(f"Глобальный минимум: {final_state}, Phi = {landscape(final_state):.4f}")
```

---

## Repository Structure / Структура репозитория {#repository-structure--структура-репозитория}

```text
├── theory/                  # Full mathematical theory (LaTeX)
│                            # Полная математическая теория (LaTeX)
├── paradox_generators/      # 4 smart foam generator classes
│                            # 4 класса генераторов умной пены
├── bulldozer_engine/        # trench_detector, paradox_injector, advection_N
├── metrics/                 # Paradox genius metrics
│                            # Оценка гениальности парадокса
├── experiments/             # Reproducible experiments (incl. Alania)
│                            # Воспроизводимые эксперименты (в т.ч. Alania)
├── dashboard/               # Streamlit landscape viz before/after attack
│                            # Streamlit-визуализация ландшафта до/после атаки
├── tests/                   # Unit tests / Модульные тесты
└── examples/                # Demo scripts / Демо-скрипты
```

---

## Usage Examples / Примеры использования {#usage-examples--примеры-использования}

### 1. Bulldozer vs “Saddle” (Saddam function)  
### 1. Бульдозер против «седла» (функция Сэддама)

```bash
python experiments/bulldozer_vs_saddam.py
```

Shows how plain gradient descent gets stuck in a false minimum, while the paradox-enabled bulldozer finds the global one.  
Показывает, как обычный градиентный спуск застревает в ложном минимуме, а бульдозер с парадоксами находит глобальный.

---

### 2. Quantum gravity search (scientometric experiment)  
### 2. Поиск квантовой гравитации (наукометрический эксперимент)

```bash
python experiments/science_frontier.py
```

Generates paradoxes from simultaneous application of GR and QM, then zeros them into a covariant theory.  
Генерирует парадоксы из одновременного применения ОТО и КМ, обнуляет их в ковариантную теорию.

---

### 3. Alan constitution  
### 3. Аланская конституция

```bash
python experiments/alania_constitution.py
```

Spawns ethical coexistence paradoxes and zeros them into Alan laws (principle: “do no harm + zero carefully”).  
Порождает этические парадоксы совместного бытия и обнуляет их в аланские законы (принцип «не навреди + обнуляй осторожно»).

---

## Citation / Цитирование {#citation--цитирование}

If you use this repository in research, please cite:  
Если вы используете этот репозиторий в исследовании, пожалуйста, цитируйте:

> Oleg Bits, *GRA-Paradox-Zeroing: Tactical Paradox Generation and Trench Zeroing for AGI Landscapes*, 2026, GitHub: qqewq/GRA-Paradox-Zeroing.

---

## License / Лицензия {#license--лицензия}

MIT (c) 2026 Oleg Bits  
MIT (c) 2026 Oleg Bits