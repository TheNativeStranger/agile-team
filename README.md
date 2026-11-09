# agile-team

Spring Boot ve OpenShift üzerinde Kafka projeleri için, Baş Mimar'ın yönettiği özel Claude Code ekibi.

Plan çizimi: [docs/architecture/ekip-plani.drawio](docs/architecture/ekip-plani.drawio)

## Ekip
| Rol | Ajan | İş |
|---|---|---|
| Baş Mimar | `solution-architect` | Ekibi yönetir, mimari kararlar, draw.io çizimleri |
| Solution Designer | `solution-designer` | Sözleşmeler, şemalar, veri modeli |
| Kafka Uzmanı | `kafka-expert` | Kafka incelemesi, yalnızca okur |
| Java Developer | `java-developer` | Spring Boot kodu, kodu yalnızca o değiştirir |
| QA Tester | `qa-tester` | Test yazar ve çalıştırır |
| Operasyon | `ops-engineer` | OpenShift, dağıtım ve geri alma incelemesi |

## Kurulum
```bash
claude plugin marketplace add ~/Desktop/projects/agile-team
claude plugin install agile-team@agile-team-local
```

Bir değişiklikten sonra `plugin.json` ve `marketplace.json` içindeki sürümü artır, ardından:

```bash
claude plugin marketplace update agile-team-local
claude plugin update agile-team@agile-team-local
```

## Kullanım
Java projesinin klasöründe `/agile-team:mimar <iş tanımı>` yaz.

## Gizlilik
Depo özeldir. Çizimler yalnızca yerel `.drawio` dosyası olarak üretilir, uzak bir servise gönderilmez. Şirkete ait kod, müşteri verisi ve gizli anahtar bu depoya konmaz.

## Lisans
Kişisel kullanım içindir. `skills/drawio/SKILL.md` jgraph/drawio-mcp projesinden alınmıştır (Apache-2.0), bkz. `skills/drawio/NOTICE`.
