

> [!info] Por qué "Custom"
> Esta escala es **construcción propia**, no adoptada. No desciende de TRL: TRL mide qué tan
> probada está una tecnología en su entorno; esta mide qué tan bien **empaquetamos** algo para
> reuso interno — los niveles 2 a 5 no tienen equivalente en TRL.
> La procedencia y la defensa están en `decisions/adr/0011-scale-provenance.md`.

## Readiness levels - Custom

|#|Level|Meaning|Evidence that establishes it|
|---|---|---|---|
|**0**|Not available|No supported realization.|—|
|**1**|Available or project-proven|The technology exists and can do it, or one team has built it and it works. Not separable from their application, not reusable.|The application, or the vendor capability|
|**2**|Approved|Cleared for enterprise use. Each team assembles the solution itself.|The approval record|
|**3**|Standardized|A published standard and an architecture pattern or reference architecture exist.|The standard · the pattern document|
|**4**|Industrialized|Reusable solution building blocks: IaC, security baseline, observability, CI/CD, implementation guidance, support model. Teams self-serve a compliant instance and operate it.|The module or template repository · a team that used it|
|**5**|Productized|An exposed endpoint with a contract. Consumers call it; the platform operates it.|The endpoint · its service levels · its operational owner · its consumers|


## Comparador World Bank — *es un modelo de MADUREZ, no de readiness*

> [!warning] Corregido el 4 de septiembre de 2026
> Esta lámina estaba archivada aquí como *"readiness levels - World Bank"*. **No lo es.**
> Se titula **"Maturity Model"** y sus niveles son 1 Initial · 2 Emerging · 3 Consolidating ·
> 4 Integrating · 5 Optimizing — CMMI clásico. El "readiness" del título del deck
> (*AI Readiness of WB Data*) se refiere al **objeto** evaluado, no a una escala de readiness.
>
> Sirve como corroboración de nuestra escala de **madurez**, no de la de preparación.
> Análisis completo, sus cuatro dimensiones y la regla de manejo:
> `decisions/adr/0011-scale-provenance.md` §5.
>
> **Grado D** (no público, sin fecha ni URL, *Official Use Only*): uso interno únicamente,
> no va al registro de fuentes, no se reproduce fuera del Banco.

![[assets/Pasted image 20260903142035.png]]


