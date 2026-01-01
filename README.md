# SecurePass Generator 🔒

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18119423.svg)](https://doi.org/10.5281/zenodo.18119423)
[![CC0 License](https://img.shields.io/badge/License-CC0_1.0_Universal-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

[English](#english) | [Español](#español) | [Português](#português)

---

## English

Advanced GUI password generator with cryptographic security and entropy analysis

![Password Generator Demo](demo-screenshot.png)

### Features ✨

- **Custom Character Sets**:
  - Uppercase/Lowercase letters
  - Digits
  - Special characters
  - Ambiguous character exclusion (l,1,O,0)

- **Security Features**:
  - Cryptographically secure generation (`secrets` module)
  - Real-time entropy calculation (bits)
  - Strength classification (Weak/Moderate/Strong)

- **Advanced Controls**:
  - Length selection (8-32 characters)
  - Input validation
  - Copy feedback animation

- Modern themeable GUI (ttkthemes)
- Automatic dependency management
- Cross-platform compatibility

### Installation 🛠️

```bash
# Clone repository
git clone https://github.com/yourusername/securepass-generator.git
cd securepass-generator

# Install requirements
pip install -r requirements.txt
```

### Usage 🚀

```bash
python main.py
```

**Interface Guide**:
1. Select character types using checkboxes
2. Enable/disable ambiguous characters
3. Choose password length (8-32)
4. Generate password with strength feedback
5. Copy to clipboard with visual confirmation

### Dependencies 📦

| Package     | Version  | Purpose                |
|-------------|----------|------------------------|
| `ttkthemes` | 3.2.2    | Modern UI Styling      |
| `tkinter`   | Built-in | GUI Framework          |
| `secrets`   | Built-in | Cryptographic Security |
| `math`      | Built-in | Entropy Calculation    |

Full list in [requirements.txt](requirements.txt)

### License 📜

This project is released under the [CC0 1.0 Universal](LICENSE) license:

```text
You are free to:
- Use commercially
- Modify and redistribute
- Use without attribution
- Patent and trademark use

No warranties provided. Use at your own risk.
```

### Contributions 🤝

We welcome community improvements:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push branch (`git push origin feature/improvement`)
5. Open Pull Request

---

**Security Implementation**: This tool uses Python's `secrets` module for cryptographically secure password generation. Entropy calculations follow NIST SP 800-63 recommendations for password strength estimation.

---

## Español

Generador avanzado de contraseñas con interfaz gráfica, seguridad criptográfica y análisis de entropía

![Demostración del Generador de Contraseñas](demo-screenshot.png)

### Características ✨

- **Conjuntos de Caracteres Personalizados**:
  - Letras mayúsculas/minúsculas
  - Dígitos
  - Caracteres especiales
  - Exclusión de caracteres ambiguos (l,1,O,0)

- **Características de Seguridad**:
  - Generación criptográficamente segura (módulo `secrets`)
  - Cálculo de entropía en tiempo real (bits)
  - Clasificación de fortaleza (Débil/Moderada/Fuerte)

- **Controles Avanzados**:
  - Selección de longitud (8-32 caracteres)
  - Validación de entrada
  - Animación de confirmación de copia

- Interfaz gráfica moderna con temas (ttkthemes)
- Gestión automática de dependencias
- Compatibilidad multiplataforma

### Instalación 🛠️

```bash
# Clonar repositorio
git clone https://github.com/yourusername/securepass-generator.git
cd securepass-generator

# Instalar requisitos
pip install -r requirements.txt
```

### Uso 🚀

```bash
python main.py
```

**Guía de Interfaz**:
1. Selecciona tipos de caracteres usando casillas de verificación
2. Habilita/deshabilita caracteres ambiguos
3. Elige la longitud de la contraseña (8-32)
4. Genera la contraseña con retroalimentación de fortaleza
5. Copia al portapapeles con confirmación visual

### Dependencias 📦

| Paquete     | Versión  | Propósito                     |
|-------------|----------|-------------------------------|
| `ttkthemes` | 3.2.2    | Estilización Moderna de UI    |
| `tkinter`   | Integrado| Framework de Interfaz Gráfica |
| `secrets`   | Integrado| Seguridad Criptográfica       |
| `math`      | Integrado| Cálculo de Entropía           |

Lista completa en [requirements.txt](requirements.txt)

### Licencia 📜

Este proyecto se publica bajo la licencia [CC0 1.0 Universal](LICENSE):

```text
Eres libre de:
- Usar comercialmente
- Modificar y redistribuir
- Usar sin atribución
- Uso de patentes y marcas registradas

Sin garantías. Úsalo bajo tu propio riesgo.
```

### Contribuciones 🤝

Damos la bienvenida a mejoras de la comunidad:
1. Haz fork del repositorio
2. Crea una rama de características (`git checkout -b feature/improvement`)
3. Confirma los cambios (`git commit -am 'Agregar nueva característica'`)
4. Empuja la rama (`git push origin feature/improvement`)
5. Abre un Pull Request

---

**Implementación de Seguridad**: Esta herramienta utiliza el módulo `secrets` de Python para la generación criptográficamente segura de contraseñas. Los cálculos de entropía siguen las recomendaciones NIST SP 800-63 para la estimación de la fortaleza de contraseñas.

---

## Português

Gerador avançado de senhas com interface gráfica, segurança criptográfica e análise de entropia

![Demonstração do Gerador de Senhas](demo-screenshot.png)

### Recursos ✨

- **Conjuntos de Caracteres Personalizados**:
  - Letras maiúsculas/minúsculas
  - Dígitos
  - Caracteres especiais
  - Exclusão de caracteres ambíguos (l,1,O,0)

- **Recursos de Segurança**:
  - Geração criptograficamente segura (módulo `secrets`)
  - Cálculo de entropia em tempo real (bits)
  - Classificação de força (Fraca/Moderada/Forte)

- **Controles Avançados**:
  - Seleção de comprimento (8-32 caracteres)
  - Validação de entrada
  - Animação de confirmação de cópia

- Interface gráfica moderna com temas (ttkthemes)
- Gerenciamento automático de dependências
- Compatibilidade multiplataforma

### Instalação 🛠️

```bash
# Clonar repositório
git clone https://github.com/yourusername/securepass-generator.git
cd securepass-generator

# Instalar requisitos
pip install -r requirements.txt
```

### Uso 🚀

```bash
python main.py
```

**Guia da Interface**:
1. Selecione tipos de caracteres usando caixas de seleção
2. Habilite/desabilite caracteres ambíguos
3. Escolha o comprimento da senha (8-32)
4. Gere a senha com feedback de força
5. Copie para a área de transferência com confirmação visual

### Dependências 📦

| Pacote      | Versão   | Propósito                      |
|-------------|----------|--------------------------------|
| `ttkthemes` | 3.2.2    | Estilização Moderna de UI      |
| `tkinter`   | Integrado| Framework de Interface Gráfica |
| `secrets`   | Integrado| Segurança Criptográfica        |
| `math`      | Integrado| Cálculo de Entropia            |

Lista completa em [requirements.txt](requirements.txt)

### Licença 📜

Este projeto é lançado sob a licença [CC0 1.0 Universal](LICENSE):

```text
Você é livre para:
- Usar comercialmente
- Modificar e redistribuir
- Usar sem atribuição
- Uso de patentes e marcas registradas

Sem garantias. Use por sua conta e risco.
```

### Contribuições 🤝

Agradecemos melhorias da comunidade:
1. Faça fork do repositório
2. Crie uma branch de recurso (`git checkout -b feature/improvement`)
3. Confirme as alterações (`git commit -am 'Adicionar novo recurso'`)
4. Envie a branch (`git push origin feature/improvement`)
5. Abra um Pull Request

---

**Implementação de Segurança**: Esta ferramenta usa o módulo `secrets` do Python para geração criptograficamente segura de senhas. Os cálculos de entropia seguem as recomendações NIST SP 800-63 para estimativa de força de senha.
